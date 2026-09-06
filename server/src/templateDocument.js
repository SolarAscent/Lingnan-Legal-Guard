import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';
import Docxtemplater from 'docxtemplater';
import PizZip from 'pizzip';
import { createContractDocx } from './contractDocument.js';
import { getTemplate } from './templateRegistry.js';

export async function createTemplateDocx(templateId, fields, outputPath) {
  const template = getTemplate(templateId);
  if (template.id === 'sale') return createContractDocx(fields, outputPath);
  const bytes = await readFile(new URL(`../templates/${template.id}.docx`, import.meta.url));
  const document = new Docxtemplater(new PizZip(bytes), {
    delimiters: { start: '{{', end: '}}' }, paragraphLoop: true, linebreaks: true,
    nullGetter: () => '________',
  });
  const values = Object.fromEntries(template.fields.map((field) => {
    const input = fields[field.key];
    let value = typeof input === 'string' ? input.trim() : '';
    if (value && field.type === 'date') {
      const [year, month, day] = value.split('-');
      value = `${year}年${Number(month)}月${Number(day)}日`;
    }
    // Empty co-borrower removes the optional block; names never substitute signatures.
    return [field.key, value || (field.key === 'coBorrower' ? '' : '________')];
  }));
  document.render(values);
  await mkdir(dirname(outputPath), { recursive: true });
  await writeFile(outputPath, document.getZip().generate({ type: 'nodebuffer', compression: 'DEFLATE' }));
}
