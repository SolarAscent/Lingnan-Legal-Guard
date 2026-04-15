将 `lg-robot.svg` 替换为你自己的小人图片：

步骤：
1. 准备图片
   - 推荐：透明背景的 PNG/SVG，或正方形图片（建议 256x256 或更大）。
   - 文件名建议：`lg-robot.png` 或 `lg-robot.svg`。

2. 放置图片
   - 把文件放到项目的 `assets` 目录（本仓库路径：`e:\Mooctest\Legal-Guard\assets`）。
   - 覆盖已有 `lg-robot.svg` 即可。

3. 可选：使用 PNG
   - 如果使用 PNG，请将 `demo.html` 中 `img` 的 src 从 `assets/lg-robot.svg` 改为 `assets/lg-robot.png`。

4. 完成后在浏览器打开 `demo.html` 查看效果。

注意：
- 本项目示例使用 `assets/lg-robot.svg` 作为占位符，已加入回退逻辑（若图片加载失败，会显示箭头图标）。
- 如果你需要我帮你把你提供的图片上传并替换，请把图片文件拖到工作区或给我上传链接，我会替你放到 `assets` 并更新引用。
