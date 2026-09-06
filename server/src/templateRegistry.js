import { readFileSync } from 'node:fs';
import { z } from 'zod';

export const templates = JSON.parse(readFileSync(new URL('../templates/catalog.json', import.meta.url), 'utf8'));
export function getTemplate(id = 'sale') {
  const template = templates.find((item) => item.id === id);
  if (!template) throw Object.assign(new Error('请选择有效的合同模板'), { statusCode: 400, code: 'INVALID_TEMPLATE' });
  return template;
}
const validDate = (value) => /^\d{4}-\d{2}-\d{2}$/.test(value) && Number.isFinite(Date.parse(value)) && new Date(value).toISOString().slice(0, 10) === value;
export function schemaFor(template) {
  const shape = {};
  for (const field of template.fields) {
    let value = z.string().trim().max(field.maxLength, `${field.label}不能超过${field.maxLength}个字符`)
      .refine((v) => !/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(v), '请去除不支持的控制字符');
    if (field.required) value = value.refine((v) => v.length > 0, `${field.label}为必填项`);
    if (field.type === 'date') value = value.refine((v) => !v || validDate(v), `${field.label}须为有效日期`);
    if (field.type === 'number') value = value.refine((v) => !v || (/^\d+(\.\d+)?$/.test(v) && Number.isFinite(Number(v))), `${field.label}须为非负数字`);
    if (field.options) value = value.refine((v) => !v || field.options.includes(v), `请选择${field.label}`);
    shape[field.key] = field.required ? value : value.optional().default('');
  }
  return z.object(shape).superRefine((values, ctx) => {
    const issue = (path, message) => ctx.addIssue({ code: 'custom', path: [path], message });
    if (values.startDate && values.endDate && values.endDate < values.startDate) issue('endDate', '结束日期不能早于开始日期');
    if (values.loanDate && values.dueDate && values.dueDate < values.loanDate) issue('dueDate', '到期日期不能早于收到借款日期');
    for (const key of ['principal', 'landArea', 'serviceArea']) {
      if (values[key] && Number(values[key]) <= 0) issue(key, '金额或面积必须大于零');
    }
    if (values.restDays && Number(values.restDays) > 7) issue('restDays', '每周休息天数不能超过7天');
    if (values.depositPercent && Number(values.depositPercent) > 100) issue('depositPercent', '订金比例不能超过100%');
    if (values.coBorrowerId && !values.coBorrower) issue('coBorrower', '填写共同借款人证件号码时，请同时填写姓名');
  });
}
export function parseContractRequest(body) {
  const template = getTemplate(body?.templateId);
  const result = schemaFor(template).safeParse(body?.fields ?? body);
  return { template, result };
}
