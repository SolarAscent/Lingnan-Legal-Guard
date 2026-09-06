# 合同模板维护

| 板块 | templateId | 内容与来源 |
| --- | --- | --- |
| 一 | sale | 原有 GF-2025-0151 买卖合同生成器，八项字段兼容旧请求 |
| 二 | land-lease | GF-2021-2606 农村土地经营权出租合同，使用说明、十三条正文和附件清单 |
| 三 | picking-labor | 用户提供采茶叶劳务合同汇编中的第一份完整范本，保留十一条正文；不拼接其他范本 |
| 四 | cooperative | 社员加入农民专业合作社合同，适用畜禽养殖合作社 |
| 五 | iou | 承德市司法局个人借条范本，提取借条正文并把案例姓名、日期、利率替换为填写项 |
| 六 | farm-service | 农业生产托管服务合同，九条正文及完整农作物生产托管服务标准指引 |

`source/` 保存用户提供的五份原始 Word，`source/manifest.json` 记录 SHA-256。原文件未经修改。二、四、六的正文是图片，已转为可编辑段落和表格；分页随内容长度变化，并非原扫描版的逐页复刻。第四份图片右侧被裁切，以同源 [法蚕文本](https://www.facan.com/doc/7liqdnt2m9) 补齐；第六份 OCR 对照 [农业农村部正文](https://hzjjs.moa.gov.cn/gzdt/202006/t20200612_6346445.htm) 校核。

租金方式、地块扩展等原文选择/空格整理为带提示的填写项。未填写的可选项输出横线；每一项服务标准均可填写。借条须手动确认实际收到借款，语音或 AI 不会代勾确认。签名、盖章留白。生成后仍需核对并补齐适用约定。

## 字段与生成

- `catalog.json` 是前后端共享的字段定义（顺序、必填、类型、限长、分组）。
- `GET /api/templates` 返回六项模板元数据。
- `POST /api/contracts` 使用 `{ "templateId": "land-lease", "fields": { ... } }`；旧版不带 templateId 的平铺请求仍使用板块一。
- `POST /api/speech/cantonese` 接受同样的 `templateId`，仅提取该模板字段。
- Node 通过 `docxtemplater` / `pizzip` 填充 `{{field}}`，转义 XML、支持换行；模板路径由服务端白名单确定。
- AI 服务网络故障、余额不足或限流时按原始填写生成，页面明确显示未完成 AI 检查。AI 明确拒绝或返回无效检查结果时仍阻止生成。
- 元数据随生成文件保存，下载名称对应所选合同。修改表单或切换模板后前端清除旧预览，避免误下载。
- LibreOffice 每次转换使用独立配置目录，支持并发生成。服务器需要中文字体（Dockerfile 已安装 `fonts-noto-cjk`）。

## 修改与验证

修改 `server/scripts/build_templates.py` 后，用安装有 `python-docx` 的 Python 执行：

```sh
python3 server/scripts/build_templates.py
npm --prefix server test
npm --prefix vue-legal-guard run build
# 启动后端和 LibreOffice 后：
TEST_BASE_URL=http://127.0.0.1:3001 npm --prefix server run test:api
```

测试覆盖全部模板字段实际写入 DOCX、必填/日期/金额校验、模板隔离、AI 不改写约定、语音不代确认收款、六类 DOCX/PDF/预览接口。修改 Word 后还应逐页渲染检查中文、跨页表格、签署位置，并至少用一组长文本核对版面。

## 生产更新

保留现有环境变量、Caddy/TLS 配置和 `storage/generated`。在新镜像上完成健康检查与六类生成测试后切换容器。将生成目录挂载到持久化存储，旧容器与旧镜像保留作回滚；不要直接删除现有容器内的生成文件。
