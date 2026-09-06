import assert from 'node:assert/strict';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve, join } from 'node:path';
const base = process.env.TEST_BASE_URL || 'http://127.0.0.1:3001';
const out = process.env.TEST_OUTPUT_DIR ? resolve(process.env.TEST_OUTPUT_DIR) : null;
if (out) await mkdir(out, { recursive: true });
const { templates } = await (await fetch(base + '/api/templates')).json();
assert.equal(templates.length, 6);
const examples = {
  sale: { partyA:'测试农产品采购公司',partyB:'测试种植合作社',productName:'鹰嘴桃',quantity:'1000 斤',unitPrice:'12 元/斤',totalPrice:'12000',deliveryTime:'2026 年 10 月 1 日',deliveryPlace:'测试村农产品收购站' },
  'land-lease': { partyA:'测试出租人',partyB:'测试承租人',landArea:'10',landLocation:'测试县测试镇测试村一号田',landUse:'种植水稻',startDate:'2026-10-01',endDate:'2027-09-30',deliveryDate:'2026-10-01',rentStandard:'每亩每年人民币800元',rentPayment:'每年10月1日前支付当年租金8000元',paymentMethod:'银行转账',parcelEast:'村道',parcelSouth:'水渠',parcelWest:'二号田',parcelNorth:'田埂',signDate:'2026-09-20' },
  'picking-labor': { partyA:'测试茶场',partyB:'测试采茶人',workPlace:'测试村一号茶园',pickingStandard:'春茶，一芽一叶，无病虫害、无杂质',startDate:'2026-10-01',endDate:'2026-10-15',payStandard:'每斤验收合格茶叶8元',acceptanceDays:'2',paymentMethod:'银行转账',workHours:'每日8:00至17:00，午休1小时',restDays:'1',insurance:'意外伤害保险' },
  cooperative: { partyA:'测试畜禽养殖专业合作社',partyB:'测试社员',signDate:'2026-10-01' },
  iou: { lender:'测试出借人',borrower:'测试借款人',loanPurpose:'购买种子和化肥',principal:'10000.00',principalChinese:'人民币壹万元整',loanTerm:'六个月',loanDate:'2026-10-01',dueDate:'2027-04-01',transferMethod:'银行转账',interestTerms:'无息',overdueTerms:'双方约定不计逾期利息',receiptConfirmed:'已确认实际收到借款',signDate:'2026-10-01' },
  'farm-service': { partyA:'测试农户',partyB:'测试农业服务合作社',county:'测试',town:'测试',village:'测试',villageGroup:'一',serviceArea:'20',crop:'水稻',serviceItems:'耕整地、种植、收获',startDate:'2026-10-01',endDate:'2027-09-30',servicePrice:'200',totalFee:'4000',serviceStandards:'按双方约定的种植计划完成作业，各环节完成后由甲方现场验收。',standard4:'旋耕',standard5:'2026年10月1日至2026年10月3日',standard24:'双方确认适用的小型水稻联合收割机' },
};
for (let i = 0; i < templates.length; i += 2) {
  await Promise.all(templates.slice(i, i+2).map(async t => {
    const body = { templateId:t.id, fields:examples[t.id] };
    const response = await fetch(base+'/api/contracts', { method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body) });
    const data = await response.json();
    assert.equal(response.status,201,JSON.stringify(data)); assert.equal(data.templateId,t.id);
    assert.deepEqual(Object.keys(data.normalizedFields).sort(),t.fields.map(f=>f.key).sort());
    for (const [key, ext] of [['docxUrl','docx'],['pdfUrl','pdf'],['previewUrl','preview.pdf']]) {
      const file = await fetch(base+data[key]); assert.equal(file.status,200);
      const buffer=Buffer.from(await file.arrayBuffer());assert.ok(buffer.length>1000);
      assert.equal(buffer.subarray(0,ext==='docx'?2:4).toString(),ext==='docx'?'PK':'%PDF');
      if (out && ext !== 'preview.pdf') await writeFile(join(out,t.id+'.'+ext),buffer);
    }
    if (out) await writeFile(join(out,t.id+'.json'),JSON.stringify(body,null,2));
    console.log('PASS',t.id,'DOCX + PDF + preview',data.id);
  }));
}
for (const body of [{templateId:'unknown'}, {templateId:'iou',fields:examples.sale}, {templateId:'land-lease',fields:{...examples['land-lease'],endDate:'2020-01-01'}}]) {
 const response=await fetch(base+'/api/contracts',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});assert.equal(response.status,400);
}
const invalidSpeech=await fetch(base+'/api/speech/cantonese',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({templateId:'unknown',audioBase64:'AA=='})});assert.equal(invalidSpeech.status,400);
const missing = await fetch(base+'/api/contracts/abcdefgh/download.pdf'); assert.equal(missing.status,404);
console.log('PASS invalid templates, mismatched schemas, dates, speech template, missing download');
