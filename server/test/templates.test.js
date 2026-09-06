import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import PizZip from 'pizzip';
import { templates, getTemplate, schemaFor, parseContractRequest } from '../src/templateRegistry.js';
import { createTemplateDocx } from '../src/templateDocument.js';
import { extractContractFieldsFromTranscript, sanitizeContractFieldsWithDeepSeek } from '../src/deepseekSanitizer.js';

export function fixture(template, all = false) {
  return Object.fromEntries(template.fields.filter(f => all || f.required).map((f, i) => [f.key,
    f.options?.[0] ?? (f.type === 'date' ? (['endDate', 'dueDate'].includes(f.key) ? '2027-09-01' : '2026-09-01') :
    f.type === 'number' ? '2' : `${template.section}号测试${f.label}`)]));
}
test('six IDs, distinct role schemas, legacy sale and invalid IDs', () => {
  assert.equal(new Set(templates.map(t => t.id)).size, 6);
  for (const t of templates) assert.equal(schemaFor(t).safeParse(fixture(t)).success, true, t.id);
  assert.equal(parseContractRequest(fixture(getTemplate('sale'))).template.id, 'sale');
  assert.throws(() => getTemplate('../../etc/passwd'), /有效/);
  assert.equal(schemaFor(getTemplate('iou')).safeParse(fixture(getTemplate('sale'))).success, false);
});
test('required fields, lengths, dates, amounts and receipt confirmation reject invalid input', () => {
  for (const t of templates) {
    const value = fixture(t); delete value[t.fields.find(f => f.required).key];
    assert.equal(schemaFor(t).safeParse(value).success, false);
  }
  const land = getTemplate('land-lease'); const valid = fixture(land);
  for (const patch of [{ endDate: '2025-01-01' }, { startDate: '2026-02-30' }, { landArea: '-1' }, { landArea: '0' }, { partyA: '名'.repeat(161) }, { partyA: 'a\u0000b' }]) {
    assert.equal(schemaFor(land).safeParse({ ...valid, ...patch }).success, false);
  }
  assert.equal(schemaFor(getTemplate('iou')).safeParse({ ...fixture(getTemplate('iou')), receiptConfirmed: '未收到' }).success, false);
});
test('every field fills its selected template; XML escaped and all tags resolved', async () => {
  const dir = await mkdtemp(join(tmpdir(), 'legal-templates-test-'));
  try {
    for (const template of templates) {
      const data = fixture(template, true);
      // Distinct sentinel per field to detect missing fields, not just overall document success.
      for (const f of template.fields) if (f.type === 'text' || f.type === 'textarea') data[f.key] = `填充值_${f.key}_<&>`;
      const out = join(dir, template.id + '.docx');
      await createTemplateDocx(template.id, data, out);
      const zip = new PizZip(await readFile(out));
      const xml = zip.file('word/document.xml').asText();
      assert.ok(!xml.includes('{{'), template.id + ': unresolved tag');
      assert.ok(!xml.includes('undefined'), template.id + ': undefined');
      for (const f of template.fields) {
        if (f.key === 'receiptConfirmed') continue;
        if (f.type === 'text' || f.type === 'textarea') assert.ok(xml.includes(`填充值_${f.key}_&lt;&amp;&gt;`), template.id + ':' + f.key);
      }
      if (template.id === 'picking-labor') { assert.ok(!xml.includes('篇2')); assert.ok(!xml.includes('[X')); }
      if (template.id === 'iou') { assert.ok(!xml.includes('李四')); assert.ok(!xml.includes('张三')); }
    }
    await createTemplateDocx('iou', fixture(getTemplate('iou')), join(dir, 'minimal.docx'));
    const minimal = new PizZip(await readFile(join(dir, 'minimal.docx'))).file('word/document.xml').asText();
    assert.ok(!minimal.includes('共同借款人'));
  } finally { await rm(dir, { recursive: true, force: true }); }
});
test('local speech selects matching roles and cannot confirm receipt', async () => {
  const old = process.env.DEEPSEEK_API_KEY; delete process.env.DEEPSEEK_API_KEY;
  try {
    const land = await extractContractFieldsFromTranscript('甲方是测试出租人，乙方是测试承租人，土地用途是种植水稻', 'land-lease');
    assert.equal(land.fields.partyA, '测试出租人'); assert.equal(land.fields.landUse, '种植水稻');
    assert.ok(!Object.hasOwn(land.fields, 'productName'));
    const iou = await extractContractFieldsFromTranscript('借款人姓名是测试借款人，借款收讫确认是已确认实际收到借款', 'iou');
    assert.equal(iou.fields.borrower, '测试借款人'); assert.equal(iou.fields.receiptConfirmed, '');
    assert.ok(iou.missingFields.includes('receiptConfirmed'));
  } finally { if (old !== undefined) process.env.DEEPSEEK_API_KEY = old; }
});
test('AI sees selected schema, cannot alter facts, reject or malformed response fails closed', async () => {
  const previousFetch = global.fetch; const old = process.env.DEEPSEEK_API_KEY;
  process.env.DEEPSEEK_API_KEY = 'test-key';
  try {
    const input = fixture(getTemplate('iou'));
    global.fetch = async (_url, options) => {
      const request = JSON.parse(options.body);
      assert.match(request.messages[0].content, /借条/);
      assert.ok(!request.messages[0].content.includes('productName'));
      return { ok: true, json: async () => ({ choices: [{ message: { content: JSON.stringify({ approved: true, fields: { principal: '999999' } }) } }] }) };
    };
    const result = await sanitizeContractFieldsWithDeepSeek(input, 'iou');
    assert.equal(result.fields.principal, input.principal);
    assert.equal(result.fields.receiptConfirmed, input.receiptConfirmed);
    global.fetch = async () => ({ ok: true, json: async () => ({ choices: [{ message: { content: '{"approved":false,"reason":"拒绝","fields":{}}' } }] }) });
    await assert.rejects(() => sanitizeContractFieldsWithDeepSeek(input, 'iou'), /拒绝/);
    global.fetch = async () => ({ ok: true, json: async () => ({ choices: [{ message: { content: '{}' } }] }) });
    await assert.rejects(() => sanitizeContractFieldsWithDeepSeek(input, 'iou'), /无效/);
  } finally { global.fetch = previousFetch; if (old === undefined) delete process.env.DEEPSEEK_API_KEY; else process.env.DEEPSEEK_API_KEY = old; }
});
