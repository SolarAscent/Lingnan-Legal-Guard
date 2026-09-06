"""Build reviewed, editable templates. Runtime generation needs Node only.
Usage: python build_templates.py --source /path/to/板块二至六合同Word版
Requires python-docx. Source documents are never modified.
"""
from pathlib import Path
import argparse, json, hashlib, shutil, re
from docx import Document
from docx.shared import Mm, Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT = Path(__file__).resolve().parents[1] / 'templates'
ROOT.mkdir(exist_ok=True)
CAT = []

def field(key, label, example='', required=False, kind='text', group='补充信息', options=None):
    d = dict(key=key, label=label, placeholder=example, required=required, type=kind, group=group, maxLength=1000 if kind=='textarea' else 160)
    if options: d['options']=options
    return d

def fs(spec, required=False, group='补充信息'):
    result=[]
    for row in spec.strip().split('\n'):
        parts=row.split('|'); key,label=parts[:2]; example=parts[2] if len(parts)>2 else ''
        kind=parts[3] if len(parts)>3 else 'text'
        result.append(field(key,label,example,required,kind,group))
    return result

def parties(a,b):
    return fs(f'partyA|{a}|请填写完整姓名或名称\npartyB|{b}|请填写完整姓名或名称',True,'基本信息')

def contacts():
    return fs('partyAId|甲方证件号码\npartyAAddress|甲方联系地址\npartyAPhone|甲方联系电话\npartyBId|乙方证件号码\npartyBAddress|乙方联系地址\npartyBPhone|乙方联系电话',group='主体补充信息')

def make(id, section, title, scenario, description, source, fields, summary):
    meta=dict(id=id,section=section,title=title,scenario=scenario,description=description,source=source,fields=fields,summary=summary,version='1.0')
    CAT.append(meta)
    doc=Document(); sec=doc.sections[0];sec.page_width=Mm(210);sec.page_height=Mm(297)
    sec.top_margin=sec.bottom_margin=Mm(22);sec.left_margin=sec.right_margin=Mm(22)
    style=doc.styles['Normal'];style.font.name='SimSun';style._element.rPr.rFonts.set(qn('w:eastAsia'),'SimSun');style.font.size=Pt(11)
    style.paragraph_format.line_spacing=1.35;style.paragraph_format.space_after=Pt(5)
    for name in ['Title','Heading 1','Heading 2']:
        s=doc.styles[name];s.font.name='SimSun';s._element.rPr.rFonts.set(qn('w:eastAsia'),'SimSun');s.font.color.rgb=__import__('docx').shared.RGBColor(0,0,0)
        s.font.size=Pt(18 if name=='Title' else 12);s.font.bold=True
    for name in ['Normal', 'Title', 'Heading 1', 'Heading 2']:
        el = doc.styles[name].element
        for border in el.xpath('./w:pPr/w:pBdr'): border.getparent().remove(border)
        for font in el.xpath('./w:rPr/w:rFonts'):
            for attr in list(font.attrib):
                if 'theme' in attr.lower(): del font.attrib[attr]
    p=doc.add_paragraph(title,'Title');p.alignment=1
    return doc,meta

def lines(doc,body):
    for s in body.strip().split('\n'):
        s=s.strip()
        if not s: continue
        if s=='---':doc.add_page_break();continue
        doc.add_paragraph(s[2:] if s.startswith('# ') else s, 'Heading 1' if s.startswith('# ') else None)

def table(doc,headers,rows,widths=None):
    t=doc.add_table(rows=1,cols=len(headers));t.style='Table Grid'
    for c,v in zip(t.rows[0].cells,headers):c.text=v
    repeat=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(repeat)
    for row in rows:
        for c,v in zip(t.add_row().cells,row):c.text=v
    if widths:
        t.autofit=False
        for col,width in zip(t.columns,widths): col.width=Mm(width)
    for row in t.rows:
        row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        for i,c in enumerate(row.cells):
            if widths: c.width=Mm(widths[i])
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(3)
                p.paragraph_format.line_spacing=1.1
                for r in p.runs:r.font.size=Pt(9)
    return t

def save(doc,meta):
    text='\n'.join(p.text for p in doc.paragraphs)+'\n'+'\n'.join(c.text for t in doc.tables for r in t.rows for c in r.cells)
    tags=set(re.findall(r'\{\{([a-zA-Z]\w*)\}\}',text))
    fields={f['key'] for f in meta['fields']}
    assert tags==fields-{'receiptConfirmed'},(meta['id'],tags-fields,fields-tags)
    assert len(fields)==len(meta['fields'])
    doc.save(ROOT/(meta['id']+'.docx'))

# Block 1 keeps the existing GF-2025-0151 generator and its public API.
CAT.append(dict(id='sale',section='一',title='农副产品买卖合同',scenario='我要买卖农产品',description='农户、合作社与采购方约定产品、价款和交货。',source='GF-2025-0151 示范文本',version='1.0',summary=['买受人与出卖人','产品数量、单价与总价','交货时间与地点','买卖合同正文及签署页'],fields=parties('甲方（买受人）','乙方（出卖人）')+fs('productName|产品名称|例如：鹰嘴桃\nquantity|数量|例如：1000 斤\nunitPrice|单价|例如：12 元/斤\ntotalPrice|总价|例如：12000 元\ndeliveryTime|交货时间|例如：2026 年 10 月 1 日\ndeliveryPlace|交货地点|请填写详细交货地址',True,'基本信息')))

fields=parties('甲方（出租方）','乙方（承租方）')+fs('landArea|出租面积（亩）|例如：10|number\nlandLocation|土地坐落|县、乡镇、村组及地块名称\nlandUse|土地用途|例如：种植水稻\nstartDate|租赁开始日期||date\nendDate|租赁结束日期||date\ndeliveryDate|土地交付日期||date\nrentStandard|租金标准|例如：每亩每年人民币 800 元|textarea\nrentPayment|租金支付安排|支付日期、周期和金额|textarea\npaymentMethod|付款方式|例如：银行汇款',True,'基本信息')+contacts()+fs('contractNumber|合同编号\npartyARepresentative|甲方法定代表人或农户代表人\npartyARepresentativeId|甲方代表人身份证号码\npartyAType|甲方经营主体类型\npartyBRepresentative|乙方法定代表人或农户代表人\npartyBRepresentativeId|乙方代表人身份证号码\npartyBType|乙方经营主体类型\nparcelCode|地块代码\nparcelEast|东至\nparcelSouth|南至\nparcelWest|西至\nparcelNorth|北至\nparcelGrade|土地等级与类型\nparcelNote|地块备注\nadditionalParcels|其他地块明细|逐块填写村组、名称、代码、四至、面积、等级类型|textarea\nassets|附属建筑和资产现状||textarea\nassetDisposal|附属建筑和资产处置方式||textarea',group='主体与地块详情')+fs('rentAdjustmentYears|租金调整周期（年）||number\nrentAdjustment|租金调整方式||textarea\naccountName|甲方收款账户名称\naccountNumber|甲方银行账号\nbankName|甲方开户行\npartyAOtherRights|甲方其他权利||textarea\nfilingDays|向发包方备案期限（日）||number\npartyAOtherDuties|甲方其他义务||textarea\npartyBOtherRights|乙方其他权利||textarea\npartyBOtherDuties|乙方其他义务||textarea\npermissions|甲方同意的投资或经营事项|改良土壤、建设附属设施等，按双方实际约定填写|textarea\nsubsidies|财政补贴归属||textarea\nriskDeposit|风险保障金及到期处理|是否缴纳、收取方、金额及处理方式|textarea\ncompensation|征收等情形下附着物及青苗补偿归属||textarea\notherTerms|其他约定||textarea\nrenewalNoticeDays|续租申请提前日数||number\nexitNoticeDays|不续租通知提前日数||number\nreturnDays|期满交还土地期限（日）||number\nfacilityDisposal|期满或依法提前收回时设施处置方式||textarea\nlateDeliveryRate|逾期交地违约金（年租金的万分之）||number\nlateDeliveryDays|逾期交地解除合同日数||number\nlateRentRate|逾期付租违约金（年租金的万分之）||number\nlateRentDays|逾期付租解除合同日数||number\nlateReturnRate|逾期还地违约金（年租金的万分之）||number\nsupplement|补充条款||textarea\ncopies|合同份数||number\notherHolder|其他合同持有人\nsignDate|签订日期||date\nsignPlace|签订地点\nattachmentDetails|附件清单情况|证件、权属证明、四至附图及其他附件的份数、页数|textarea',group='租金与其他约定')
d,m=make('land-lease','二','农村土地经营权出租合同','我要出租或承租土地','填写土地、租期与租金，明确出租方和承租方。','GF-2021-2606 示范文本',fields,['双方及地块明细','土地用途、租期、交付','租金、权利义务及违约责任','十三条正文、签署页与附件清单'])
lines(d,'''合同编号：{{contractNumber}}
# 使用说明
本合同为示范文本，由农业农村部与国家市场监督管理总局联合制定，供农村土地（耕地）经营权出租（含转包）的当事人签订合同时参照使用。
合同签订前，双方当事人应当仔细阅读本合同内容，特别是其中具有选择性、补充性、填充性、修改性的内容；对合同中的专业用词理解不一致的，可向当地农业农村部门或农村经营管理部门咨询。
合同签订前，工商企业等社会资本通过出租取得土地经营权的，应当依法履行资格审查、项目审核和风险防范等相关程序。
本合同文本中相关条款后留有空白行，供双方自行约定或者补充约定。双方当事人依法可以对文本条款的内容进行修改、增补或者删减。合同签订生效后，未被修改的文本印刷文字视为双方同意内容。
双方当事人应当结合具体情况选择本合同协议条款中所提供的选择项，同意的在选择项前的□打√，不同意的打×。本合同文本中涉及到的选择、填写内容以手写项为优先。当事人订立合同的，应当在合同书上签字、盖章或者按指印。
本合同文本“当事人”部分，自然人填写身份证号码，农村集体经济组织填写农业农村部门赋予的统一社会信用代码，其他市场主体填写市场监督管理部门赋予的统一社会信用代码。
本合同编号由县级以上农业农村部门或农村经营管理部门指导乡（镇）人民政府农村土地承包管理部门按统一规则填写。
---
根据《中华人民共和国民法典》《中华人民共和国农村土地承包法》和《农村土地经营权流转管理办法》等相关法律法规，本着平等、自愿、公平、诚信、有偿的原则，经甲乙双方协商一致，就土地经营权出租事宜，签订本合同。
# 一、当事人
甲方（出租方）：{{partyA}}
社会信用代码或身份证号码：{{partyAId}}
法定代表人（负责人/农户代表人）：{{partyARepresentative}}
代表人身份证号码：{{partyARepresentativeId}}
联系地址：{{partyAAddress}}    联系电话：{{partyAPhone}}
经营主体类型：{{partyAType}}
乙方（承租方）：{{partyB}}
社会信用代码或身份证号码：{{partyBId}}
法定代表人（负责人/农户代表人）：{{partyBRepresentative}}
代表人身份证号码：{{partyBRepresentativeId}}
联系地址：{{partyBAddress}}    联系电话：{{partyBPhone}}
经营主体类型：{{partyBType}}
# 二、租赁物
（一）经自愿协商，甲方将 {{landArea}} 亩土地经营权（具体见下表及附图）出租给乙方。
''')
table(d,['村组及地块名称','地块代码','东至','南至','西至','北至','等级类型','备注'],[['{{landLocation}}','{{parcelCode}}','{{parcelEast}}','{{parcelSouth}}','{{parcelWest}}','{{parcelNorth}}','{{parcelGrade}}','{{parcelNote}}']])
lines(d,'''其他地块明细（如有）：{{additionalParcels}}
（二）出租土地上的附属建筑和资产情况现状描述：{{assets}}
出租土地上的附属建筑和资产的处置方式描述（可另附件）：{{assetDisposal}}
# 三、出租土地用途
出租土地用途为：{{landUse}}
# 四、租赁期限
租赁期限自 {{startDate}} 起至 {{endDate}} 止。
# 五、出租土地交付时间
甲方应于 {{deliveryDate}} 前完成土地交付。
# 六、租金及支付方式
（一）租金标准
双方当事人约定的租金标准：{{rentStandard}}
可约定现金（每亩每年人民币金额）、实物或实物折资计价（每亩每年实物数量、品种及按市场价或国家最低收购价折合成货币），或其他标准。
租金变动：根据当地土地流转价格水平，每 {{rentAdjustmentYears}} 年调整一次租金。具体调整方式：{{rentAdjustment}}
（二）租金支付
双方当事人约定的租金支付安排（一次性支付、分期支付或其他，写明日期和金额）：{{rentPayment}}
（三）付款方式
双方当事人约定的付款方式：{{paymentMethod}}
甲方账户名称：{{accountName}}    银行账号：{{accountNumber}}
开户行：{{bankName}}
# 七、甲方的权利和义务
（一）甲方的权利
1. 要求乙方按合同约定支付租金；
2. 监督乙方按合同约定的用途依法合理利用和保护出租土地；
3. 制止乙方损害出租土地和农业资源的行为；
4. 租赁期限届满后收回土地经营权；
5. 其他：{{partyAOtherRights}}。
（二）甲方的义务
1. 按照合同约定交付出租土地；
2. 合同生效后 {{filingDays}} 日内依据《中华人民共和国农村土地承包法》第三十六条的规定向发包方备案；
3. 不得干涉和妨碍乙方依法进行的农业生产经营活动；
4. 其他：{{partyAOtherDuties}}。
# 八、乙方权利和义务
（一）乙方的权利
1. 要求甲方按照合同约定交付出租土地；
2. 在合同约定的期限内占有农村土地，自主开展农业生产经营并取得收益；
3. 经甲方同意，乙方依法投资改良土壤，建设农业生产附属、配套设施，并有权按照合同约定对其投资部分获得合理补偿；
4. 租赁期限届满，有权在同等条件下优先承租；
5. 其他：{{partyBOtherRights}}。
（二）乙方的义务
1. 按照合同约定及时接受出租土地并按照约定向甲方支付租金；
2. 在法律法规政策规定和合同约定允许范围内合理利用出租土地，确保农地农用，符合当地粮食生产等产业规划，不得弃耕抛荒，不得破坏农业综合生产能力和农业生态环境；
3. 依据有关法律法规保护出租土地，禁止改变出租土地的农业用途，禁止占用出租土地建窑、建坟或者擅自在出租土地上建房、挖砂、采石、采矿、取土等，禁止占用出租的永久基本农田发展林果业和挖塘养鱼；
4. 其他：{{partyBOtherDuties}}。
# 九、其他约定
（一）甲方同意乙方依法开展的事项（投资改良土壤、建设农业生产附属配套设施、以土地经营权融资担保、再流转土地经营权或其他）：{{permissions}}
（二）该出租土地的财政补贴等归属：{{subsidies}}
（三）风险保障金是否缴纳、收取方、金额及合同到期后的处理：{{riskDeposit}}
（四）本合同期限内，出租土地被依法征收、征用、占用时，有关地上附着物及青苗补偿费的归属：{{compensation}}
（五）其他事项：{{otherTerms}}
# 十、合同变更、解除和终止
（一）合同有效期间，因不可抗力因素致使合同全部不能履行时，本合同自动终止，甲方将合同终止日至租赁到期日的期限内已收取租金退还给乙方；致使合同部分不能履行的，其他部分继续履行，租金可以作相应调整。
（二）如乙方在合同期满后需要继续经营该出租土地，必须在合同期满前 {{renewalNoticeDays}} 日内书面向甲方提出申请。如乙方不再继续经营的，必须在合同期满前 {{exitNoticeDays}} 日内书面通知甲方，并在合同期满后 {{returnDays}} 日内将原出租的土地交还给甲方。
（三）合同到期或者未到期由甲方依法提前收回出租土地时，乙方依法投资建设的农业生产附属、配套设施处置方式：{{facilityDisposal}}
可约定由甲方无偿处置、经有资质的第三方评估或双方协商后由甲方支付价款购买、由乙方恢复原状，或其他方式。
# 十一、违约责任
（一）任何一方违约给对方造成损失的，违约方应承担赔偿责任。
（二）甲方应按合同规定按时向乙方交付土地，逾期一日应向乙方支付年租金的万分之 {{lateDeliveryRate}} 作为违约金。逾期超过 {{lateDeliveryDays}} 日，乙方有权解除合同，甲方应当赔偿损失。
（三）甲方出租的土地存在权属纠纷或经济纠纷，致使合同全部或部分不能履行的，甲方应当赔偿损失。
（四）甲方违反合同约定擅自干涉和破坏乙方的生产经营，致使乙方无法进行正常的生产经营活动的，乙方有权解除合同，甲方应当赔偿损失。
（五）乙方应按照合同规定按时足额向甲方支付租金，逾期一日乙方应向甲方支付年租金的万分之 {{lateRentRate}} 作为违约金。逾期超过 {{lateRentDays}} 日，甲方有权解除合同，乙方应当赔偿损失。
（六）乙方擅自改变出租土地的农业用途、弃耕抛荒连续两年以上、给出租土地造成严重损害或者严重破坏土地生态环境的，甲方有权解除合同、收回该土地经营权，并要求乙方赔偿损失。
（七）合同期限届满的，乙方应当按照合同约定将原出租土地交还给甲方，逾期一日应向甲方支付年租金的万分之 {{lateReturnRate}} 作为违约金。
# 十二、合同争议解决方式
本合同发生争议的，甲乙双方可以协商解决，也可以请求村民委员会、乡（镇）人民政府等调解解决。当事人不愿协商、调解或者协商、调解不成的，可以依据《中华人民共和国农村土地承包法》第五十五条的规定向农村土地承包仲裁委员会申请仲裁，也可以直接向人民法院起诉。
# 十三、附则
（一）本合同未尽事宜，经甲方、乙方协商一致后可签订补充协议。补充协议与本合同具有同等法律效力。
补充条款（可另附件）：{{supplement}}
（二）本合同自甲乙双方签字、盖章或者按指印之日起生效。本合同一式 {{copies}} 份，由甲方、乙方、农村集体经济组织、乡（镇）人民政府农村土地承包管理部门、{{otherHolder}}，各执一份。
甲方（签字、盖章或按指印）：________________
法定代表人（负责人/农户代表人）签字：________________
乙方（签字、盖章或按指印）：________________
法定代表人（负责人/农户代表人）签字：________________
签订时间：{{signDate}}    签订地点：{{signPlace}}
# 附件清单
''')
table(d,['序号','附件名称','是否具备、页数及备注'],[['1','甲方、乙方的证件复印件',''],['2','出租土地的权属证明',''],['3','出租土地四至范围附图',''],['4','其他（附属建筑及设施清单、村民会议决议书及公示材料、代办授权委托书和证件复印件等）','']])
lines(d,'附件情况：{{attachmentDetails}}')
save(d,m)

# Picking labor: only the first complete source sample.
fields=parties('甲方（雇主）','乙方（雇员）')+fs('workPlace|茶园地点|请填写具体茶园地点\npickingStandard|茶叶品种及采摘标准|请填写品种、等级和采摘要求|textarea\nstartDate|劳务开始日期||date\nendDate|劳务结束日期||date\npayStandard|劳务计价方式|例如：每斤合格茶叶 8 元\nacceptanceDays|验收期限（工作日）|例如：3|number\npaymentMethod|报酬支付方式|例如：银行转账\nworkHours|每日工作时间|例如：上午 8 点至下午 5 点\nrestDays|每周休息天数|例如：1|number',True,'基本信息')+contacts()+fs('bankName|乙方开户银行\naccountName|乙方账户名称\naccountNumber|乙方账号\ninsurance|保险名称\nlatePayRate|逾期支付每日违约金比例（%）||number\nsignDateA|甲方签订日期||date\nsignDateB|乙方签订日期||date')
d,m=make('picking-labor','三','采茶叶劳务合同','我要请人采摘茶叶','约定茶叶采摘标准、工作时间、劳务报酬与保障。','采茶叶劳务合同范本',fields,['雇主与雇员信息','茶园地点、采摘标准与期限','计酬、验收与支付','十一条正文与签署页'])
# Source document is read when --source is supplied; a text snapshot is retained for rebuilds.
parser=argparse.ArgumentParser();parser.add_argument('--source');args=parser.parse_args()
if args.source:
    source=Path(args.source);manifest=[]
    for p in sorted(source.rglob('*.docx')):
        shutil.copy2(p,ROOT/'source'/p.name)
        manifest.append(dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    (ROOT/'source'/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
source_doc=next((ROOT/'source').glob('采茶叶*.docx'))
paragraphs=[p.text for p in Document(source_doc).paragraphs]
a=paragraphs.index('篇1采茶叶劳务合同');b=paragraphs.index('篇2采茶叶劳务合同');body=paragraphs[a+1:b]
replacements={'[具体茶园地点]':'{{workPlace}}','[具体茶叶品种及采摘标准描述]':'{{pickingStandard}}','劳务期限自____年__月__日起至____年__月__日止。':'劳务期限自 {{startDate}} 起至 {{endDate}} 止。','[具体计价方式，如每斤茶叶[X]元]':'{{payStandard}}','[X]个工作日':'{{acceptanceDays}} 个工作日','[具体支付方式，如银行转账等]':'{{paymentMethod}}','[具体工作时间段，如每天上午[X]点至下午[X]点]':'{{workHours}}','[X]天':'{{restDays}} 天','[具体保险名称，如意外伤害保险等]':'{{insurance}}','[X%]':'{{latePayRate}}%','开户银行：__________________':'开户银行：{{bankName}}','账户名称：__________________':'账户名称：{{accountName}}','账号：__________________':'账号：{{accountNumber}}'}
party='A';date_count=0
for line in body:
    if line=='乙方（雇员）：':party='B'
    if line.startswith('姓名：'):line='姓名：{{party'+party+'}}'
    elif line.startswith('身份证号：'):line='身份证号：{{party'+party+'Id}}'
    elif line.startswith('地址：'):line='地址：{{party'+party+'Address}}'
    elif line.startswith('联系电话：'):line='联系电话：{{party'+party+'Phone}}'
    elif line=='日期：____年__月__日':
        date_count+=1;line='日期：{{signDate'+('A' if date_count==1 else 'B')+'}}'
    for old,new in replacements.items():line=line.replace(old,new)
    lines(d,('# ' if re.match('^[一二三四五六七八九十]+、',line) else '')+line)
save(d,m)

fields=parties('甲方（合作社）','乙方（社员）')+fs('signDate|签署日期||date',True,'基本信息')+fs('cooperativeCode|合作社统一社会信用代码\nmemberId|社员身份证号码',group='主体补充信息')
d,m=make('cooperative','四','社员加入农民专业合作社合同','我要加入养殖合作社','适用于畜禽养殖合作社入社，约定社员服务与权利义务。','社员加入农业养殖专业合作社协议',fields,['合作社与入社成员','七项养殖服务与业务约定','社员权利与义务','六条正文与签署页'])
lines(d,'''甲方（合作社）：{{partyA}}
统一社会信用代码：{{cooperativeCode}}
乙方（社员）：{{partyB}}
身份证号码：{{memberId}}
本合同各方经平等自愿协商，根据《中华人民共和国民法典》《中华人民共和国农民专业合作社法》及相关法律法规、甲方合作社（以下简称“合作社”）章程，就乙方入社事宜，签订本合同以共同遵守。
一、乙方自签订合同之日起，成为合作社的社员，享受合作社社员的一切优惠待遇，履行一切社员应尽的义务。
二、合作社以本社社员为主要服务对象，组织成员养殖畜禽、开展养殖畜禽技术培训、咨询服务，回收销售畜禽。合作社负责提供种畜禽、饲料、畜禽药、笼具、技术以及销售，实现产、供、销一条龙服务，社员可以以现金出资或者以出售产品购买生产资料的差价和二次分红作为出资。
主要业务及服务内容如下：
1.统一提供优质种畜禽，社员购买种畜禽按社员价格供给，非社员按市场价格供给。合作社所供种畜禽七天之内出现质量问题可调换。所供种畜禽均按规定防疫程序进行了疫苗。如果本社成员对购种畜禽事宜有异议，经协商也可自行购买，仍可享受社员优惠待遇。
2.统一采购配送各阶段专用全价颗粒饲料、专用畜禽药，社员购买按照成本价供给，非社员购买按市场价格供给。
3.统一回收社员的商品畜禽，承诺价格高于市场收购价，产品回收方法：一是距离近的可直接回收活畜禽，二是距离远的可安排客户定点定时回收。如果本社成员对价格有异议，经协商也可自行销售。（向合作社销售产品的可以享受加工销售增值提取的二次分红，不向合作社销售产品、购买生产资料的不能享受二次分红）。
4.统一制定并组织社员实施畜禽养殖生产质量标准，组织开展社员生产经营中的技术指导、咨询、培训和交流等活动，向社员提供养殖畜禽生产技术和经营信息等资料。
5.合作社定期举办免费的技术培训课程，请专家为广大养殖户答疑解难。同时安排专人为社员提供跟踪服务。
6.统一申报、认证认定无公害畜禽生产基地、绿色食品，提升产业结构和品牌价值。
7.本合作社本着入社自愿、退社自由的经营原则经营。
三、本社社员须履行下列义务：
遵守本社章程及其他各项规章制度，积极参加本社各项业务活动，接受本社提供的技术指导，按照本社规定的质量标准和生产技术规程从事养殖畜禽生产，履行本合同，发扬互助协作精神，谋求共同发展。
四、本合同一式二份，甲方执一份，乙方执一份。各份合同文本具有同等法律效力。
五、本合同未尽事宜，各方应另行协商并签订补充协议。
六、本合同经各方签名或盖章后生效。
（以下无合同正文）
签署时间：{{signDate}}
甲方（盖章）：________________
乙方（签名）：________________
''');save(d,m)

fields=fs('lender|出借人姓名|请填写出借人真实姓名\nborrower|借款人姓名|请填写借款人真实姓名\nloanPurpose|借款用途|例如：购买种子和化肥\nprincipal|借款本金（元）|例如：10000.00|number\nprincipalChinese|借款本金大写|例如：人民币壹万元整\nloanTerm|借款期限|例如：六个月\nloanDate|收到借款日期||date\ndueDate|还款到期日期||date\ntransferMethod|借款交付方式|例如：银行转账\ninterestTerms|借期利息约定|明确填写无息或具体利率及计息方式|textarea\noverdueTerms|逾期利息约定|按双方实际约定填写|textarea',True,'基本信息')+[field('receiptConfirmed','借款收讫确认','',True,'select','基本信息',['已确认实际收到借款'])]+fs('lenderId|出借人身份证号码\nborrowerId|借款人身份证号码\nborrowerPhone|借款人联系电话\nborrowerAddress|借款人家庭住址\ncoBorrower|共同借款人姓名（如有）\ncoBorrowerId|共同借款人身份证号码\nsignDate|立据日期||date')
d,m=make('iou','五','借条','我要写一张借条','用于已实际交付的农户小额借款，填写金额、期限和利息约定。','个人借条范本 · 承德市司法局',fields,['出借人和借款人','实收本金、交付方式与用途','借期、到期日与利息约定','借款人及可选共同借款人签署'])
lines(d,'''为 {{loanPurpose}} 之故，今收到 {{lender}}（身份证号：{{lenderId}}）以 {{transferMethod}} 出借的人民币 {{principal}} 元（大写：{{principalChinese}}），借期 {{loanTerm}}，借期利息约定：{{interestTerms}}，于 {{dueDate}} 到期时本息一并还清。如到期未还清，逾期利息约定为：{{overdueTerms}}。
收到借款日期：{{loanDate}}
立此为据。
借款人：{{borrower}}
身份证号：{{borrowerId}}
联系电话：{{borrowerPhone}}
家庭住址：{{borrowerAddress}}
借款人签名及指印：________________
{{#coBorrower}}
共同借款人：{{coBorrower}}
身份证号：{{coBorrowerId}}
共同借款人签名及指印：________________
{{/coBorrower}}
立据日期：{{signDate}}
''');save(d,m)

standards=[
('备耕','备耕时间','甲乙双方可协商约定备耕时间范围。'),
('备耕','农资采购','根据托管规模制定年度生产计划，列出种、肥、药等农资采购品种、单价、单位用量及配给方式，同时注明农资采购完成时间。'),
('备耕','农机选用','每个作业环节所用农机型号及作业能力，同时注明农机保障完成时间。'),
('耕整地','作业模式','根据当地耕作制度和生产实际，列出主要耕整地模式，如旋耕、深翻、深耕、免耕等方式。'),
('耕整地','作业时间范围','根据农时，列出耕整地作业起止时间范围及进度安排。'),
('耕整地','作业技术要求','作业要求列出所采用机械的作业深度、作业幅宽、作业速度等技术指标。'),
('耕整地','作业质量','说明各个作业环节可达到的作业效果。'),
('种子处理','种子处理工艺','如包衣等，说明使用的药剂及其成份和用量。'),
('种子处理','种子处理时间','根据农时，说明种子处理时间范围和进度安排。'),
('种子处理','种子处理要求','说明种子处理应达到的效果。'),
('种植','种植方式','按种子品类、耕作制度、地块面积、土壤特性等综合选定不同种植方式。如免耕播种、常规播种、移栽等。'),
('种植','种植时间范围','根据农时，注明作业起止时间范围和进度安排。'),
('种植','作业要求','列出所采用机械的作业幅宽、速度、深度、行距、株距，以及种、肥、药等农资使用量。非直播水田插秧在本环节说明。播种同时采用机械施底肥，列出机械作业方式（如侧施肥）、幅宽、速度、深度、种肥间距等特性并注明用肥品类品牌、施用方法和施肥量。'),
('种植','作业效果','说明可达到的作业效果。'),
('田间管理／中耕追肥','时间范围','说明进行中耕追肥的时间范围。'),
('田间管理／中耕追肥','作业要求','根据农艺技术要求，确定采用机械的作业幅宽、速度、深度等特性，并注明用肥品类、施用方法和施肥量。水田不进行中耕，但不同生育期需肥量、品类和施用方法要注明。'),
('田间管理／中耕追肥','作业效果','说明中耕追肥需要达到的指标如耕深、培土厚度、精准施肥等。'),
('田间管理／灌溉','灌溉时间范围','说明灌溉的时间范围。'),
('田间管理／灌溉','灌溉制度','按作物不同生育期需水量标准，同时结合当地实际情况制定灌溉制度，如采用水肥一体化技术。'),
('田间管理／灌溉','灌溉技术要求及作业效果','说明采用的灌溉技术要求，如灌溉水源、灌溉量等。说明灌溉应达到什么效果。'),
('田间管理／植保','植保方案','针对作物不同生育期易发生的病虫草害，制定科学防治预案，注明易爆发的时间范围、诱发环境和形成灾害的表现，列出对应适用的“农业防治、生物防治、物理防治和化学防治”等防治措施，包括相应的药剂施用方案、设备设施布置方案、天敌释放数量方案等。本部分难点在于灾害诊断，各服务主体应有专业的技术人员（或聘任兼职专家）负责防治方案的制定和实施，或将本项工作托管给专业的植保队伍。'),
('田间管理／植保','植保作业机具','列出植保方案中的作业机具，如无人机、高地隙植保机等。'),
('田间管理／植保','植保作业效果','说明植保作业的效果。'),
('作物收获','收获机机型','按作物品种、收获物、地块面积和地形条件选择收割机机型。'),
('作物收获','作业时间范围','按作物成熟度、气象条件、土壤条件等作业条件要求，确定收割时间及作业进度。'),
('作物收获','作业要求','列出所采用收割机的作业宽度、速度、秸秆切碎长度、割茬高度、籽粒损失率、果穗损失率、籽粒破碎率、秸秆抛撒不均匀率等作业特性。'),
('作物收获','作业效果','说明可达到的作业效果。'),
('秸秆处理','秸秆处理情况','根据农业生产服务主体实际情况，说明作物秸秆利用时间和利用情况，包括秸秆离田、秸秆还田。'),
('秸秆处理','秸秆离田农机具','如果秸秆离田，列出所用打包机、制粒机、运输车辆、装卸搬运机械等机具的名称、型号、作业效率等。'),
('秸秆处理','秸秆还田方式','如果秸秆还田，说明采用的还田方式，如秸秆全量粉碎还田、秸秆覆盖还田、翻埋（压）还田等。'),
('秸秆处理','秸秆还田农机具','列出所用机具名称、型号、作业效率等。'),
('烘干及仓储','烘干标准及方式','依据作物用途确定烘干时间、烘干标准和烘干方式，如热风干燥、微波干燥等。'),
('烘干及仓储','烘干机','列出采用烘干机型号、烘干效率及达到的烘干质量。'),
('烘干及仓储','仓储方式及要求','说明仓储时间和方式，一般烘干结束后应将作物按品种分类仓储，保证不混杂，粮仓保持日常通风干燥，有效保障作物品质。'),
('销售','销售约定','约定销售时间或销售价格等。'),
('技术集成解决方案','技术方案','水肥药托管方案或全程种植技术解决方案等。'),
('全程托管','产量收益与补偿','约定亩均农作物产量或亩均农作物收益，如未达到约定产量或收益，双方协商补偿金额或具体补偿方式等。'),
]
fields=parties('甲方（接受服务方）','乙方（提供服务方）')+fs('county|服务地县市区\ntown|服务地乡镇街道\nvillage|服务地村社区\nvillageGroup|村民或居民小组\nserviceArea|服务面积（亩）|例如：20|number\ncrop|托管作物|例如：水稻\nserviceItems|托管服务环节|例如：耕整地、种植、收获|textarea\nstartDate|服务开始日期||date\nendDate|服务结束日期||date\nservicePrice|服务单价（元/亩）|例如：200|number\ntotalFee|服务总费用（元）|例如：4000|number\nserviceStandards|双方约定的服务标准|写明技术、质量和验收要求；附件可逐项补充|textarea',True,'基本信息')+fs('contractNumber|合同编号\nsignDate|签订日期||date\npartyARepresentative|甲方法定代表人及身份证号\npartyAAddress|甲方地址\npartyAPhone|甲方联系方式\npartyBRepresentative|乙方法定代表人及身份证号\npartyBAddress|乙方地址\npartyBPhone|乙方联系方式\nadditionalPlots|其他托管地块及作物||textarea\nschedule|分项服务时间安排||textarea\ntotalFeeChinese|总费用大写\ndepositPercentChinese|订金比例大写\ndepositPercent|订金比例（%）||number\ndepositAmount|订金金额（元）||number\ndepositChinese|订金金额大写\nbalanceDays|验收后尾款支付期限（日）||number\nbalanceAmount|尾款金额（元）||number\nbalanceChinese|尾款金额大写\nnecessaryConditions|甲方提供的作业条件和时间||textarea\nlateFeePercentChinese|每日逾期违约金比例大写\nlateFeePercent|每日逾期违约金比例（%）||number\notherTerms|其他约定事宜||textarea\nextraStandards|其他服务事项及标准||textarea',group='主体、费用与补充约定')
for i,(group,label,hint) in enumerate(standards):fields.append(field('standard'+str(i+1),group+' · '+label,hint,False,'textarea','附件服务标准'))
d,m=make('farm-service','六','农业生产托管服务合同','我要托管农业生产','约定耕种防收等服务，填写费用、验收和逐项服务标准。','农业农村部农业生产托管服务合同示范文本',fields,['服务双方、地块与作物','服务内容、期限与费用','九条正文及签署页','可填写的完整服务标准附件'])
lines(d,'''合同编号：{{contractNumber}}
甲方（接受服务方）：{{partyA}}
乙方（提供服务方）：{{partyB}}
签订时间：{{signDate}}
# 填写说明
1.《农业生产托管服务合同示范文本》为非强制性使用文本。
2.合同当事人可结合农业生产托管服务具体情况，根据《农业生产托管服务合同示范文本》订立合同，并按照法律法规规定和合同约定承担相应的法律责任及合同权利。
甲方（接受服务方）：{{partyA}}
法定代表人及身份证号：{{partyARepresentative}}
地址：{{partyAAddress}}    联系方式：{{partyAPhone}}
乙方（提供服务方）：{{partyB}}
法定代表人及身份证号：{{partyBRepresentative}}
地址：{{partyBAddress}}    联系方式：{{partyBPhone}}
根据有关法律法规及政策规定，甲乙双方本着平等、自愿、有偿的原则，就农业生产托管服务有关事项协商一致，订立本合同。
# 第一条 服务内容
甲方将 {{county}} 县（市、区） {{town}} 乡（镇、街道） {{village}} 村（社区） {{villageGroup}} 村民小组（居民小组）的 {{serviceArea}} 亩 {{crop}} 的 {{serviceItems}} 委托给乙方开展生产托管服务。
其他地块及作物（如有）：{{additionalPlots}}
# 第二条 服务标准
甲乙双方就服务的技术标准、质量标准等协商达成约定，作为本合同附件，与本合同具有同等法律效力。【甲乙双方可参照《农作物生产托管服务标准指引》（附后），就服务事项协商约定相关标准附于本合同之后。】
# 第三条 服务期限
乙方根据农时需要和生产技术要求，在 {{startDate}} 至 {{endDate}} 期间完成甲方委托的 {{crop}} 作物 {{serviceItems}} 环节的生产托管服务。
分项服务时间安排（如有）：{{schedule}}
# 第四条 服务费用
乙方为甲方提供的生产托管服务价格为人民币 {{servicePrice}} 元/亩，服务面积 {{serviceArea}} 亩，总费用人民币 {{totalFee}} 元（大写：{{totalFeeChinese}}）。（如乙方提供服务无法按照上述方式计算服务费用，甲乙双方可根据实际服务过程中的具体情况协商约定服务费用。）
# 第五条 支付方式
甲方于本合同签订当日，支付乙方服务费用总额的百分之 {{depositPercentChinese}}（小写：{{depositPercent}}%）计人民币 {{depositAmount}} 元（大写：{{depositChinese}}）作为订金。乙方所有服务完毕并经甲方验收合格后，甲方于 {{balanceDays}} 日内支付乙方剩余服务费用人民币 {{balanceAmount}} 元（大写：{{balanceChinese}}）。（甲乙双方可约定签订合同之日支付全部服务费用，或约定完成生产托管服务后一次性支付全部服务费用，或约定从甲方委托乙方销售农作物收益中扣除服务费用。）
# 第六条 甲乙双方权利和义务
（一）甲方权利和义务
1.托管服务期间始终享有对托管地块承包经营权，托管地块产出品归甲方所有。
2.按照合同约定接受乙方提供生产托管服务，要求乙方按照《农作物生产托管服务标准指引》约定标准开展服务。对乙方服务进行监督和评价，验收服务成果。
3.有权阻止乙方实施破坏农用地和其他农业资源的行为。若因乙方故意或过失破坏托管地块种植条件、给土地造成严重损害或者严重破坏土地生态环境的，有权要求乙方赔偿由此造成的损失。
4.为乙方开展生产托管服务提供必要条件。约定内容和时间：{{necessaryConditions}}
5.法律、法规、规章和政策所规定的其他权利和义务。
（二）乙方权利和义务
1.要求甲方在约定时间内提供必要的作业条件，并对服务结果进行验收。
2.按照合同约定为甲方提供符合《农作物生产托管服务标准指引》要求的生产托管服务，并向甲方解读服务内容。
3.法律、法规、规章和政策所规定的其他权利和义务。
# 第七条 违约责任
（一）甲方逾期未支付服务费用的，从逾期之日起每日按应支付服务费用总额的百分之 {{lateFeePercentChinese}}（小写：{{lateFeePercent}}%）向乙方支付违约金，但不超过应付服务费用总额的百分之五十。
（二）乙方未按本合同约定提供服务，造成甲方损失的，应予以赔偿，具体赔偿金额和方式双方协商确定。
（三）任何一方违约所造成的损失，均由违约方负责赔偿。
（四）因不可抗力等重大因素导致本合同无法履行的，双方可以协商解除本合同，双方均不承担违约责任。
# 第八条 争议处理
甲乙双方发生争议，应协商解决。如协商不成，可以向服务所在地农业行政主管部门申请调解，也可以向服务所在地人民法院提起诉讼。
# 第九条 其他约定事项
（一）本合同自甲乙双方签字之日起生效。
（二）未尽或须调整事宜经甲乙双方协商一致可签订补充协议，补充协议与本合同具有同等法律效力。补充协议与本合同不一致，以补充协议为准。
（三）服务所在地村委会或村集体经济组织可对甲乙双方的托管服务关系予以指导和监督。
（四）本合同（包括附件《农作物生产托管服务标准指引》）一式两份，甲乙双方各持一份，具有同等法律效力。
（五）其他约定事宜：{{otherTerms}}
附件：农作物生产托管服务标准指引
甲方（签字或盖章）：________________    时间：________________
乙方（签字或盖章）：________________    时间：________________
---
# 附件 农作物生产托管服务标准指引
双方约定的技术、质量和验收标准：{{serviceStandards}}
''')
table(d,['托管服务事项','具体内容','约定标准（双方协商约定）','备注'],[[g,l,'{{standard'+str(i+1)+'}}',hint] for i,(g,l,hint) in enumerate(standards)],widths=[28,32,44,62])
lines(d,'''其他服务事项及标准：{{extraStandards}}
注：1.甲乙双方根据约定选择服务事项和服务内容，也可根据实际情况增加具体服务内容。
2.本《农作物生产托管服务标准指引》一式两份，甲乙双方各执一份，附于《农业生产托管服务合同示范文本》之后，具有同等法律效力。
甲方（签字或盖章）：________________    时间：________________
乙方（签字或盖章）：________________    时间：________________
''')
# Keep the appendix notes with both signing lines, including after long field values.
for paragraph in d.paragraphs[-5:]:
    paragraph.paragraph_format.line_spacing=1.1
    paragraph.paragraph_format.space_after=Pt(3)
    for run in paragraph.runs: run.font.size=Pt(10)
for paragraph in d.paragraphs[-5:-1]: paragraph.paragraph_format.keep_with_next=True
save(d,m)
(ROOT/'catalog.json').write_text(json.dumps(CAT,ensure_ascii=False,indent=2)+'\n')
print('Built',len(CAT),'catalog entries and 5 editable DOCX templates')
