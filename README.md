# AI_Supervision

深基课教程站（Flask 静态章节）：Python → 数据计算 → 机器学习直觉 → PyTorch → 小项目 → AI 工具 → 创新点流程 → 论文写作。

## 本地运行

```bash
pip install -r requirements.txt
python web_app.py
```

浏览器打开 http://127.0.0.1:5093

## Render 部署（必须用 Web Service，不要用 Static Site）

在 [Render Dashboard](https://dashboard.render.com/) 新建 **Web Service**（不是 Static Site），连接本仓库：

| 项 | 值 |
|---|---|
| Runtime | Python |
| Root Directory | （留空） |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn web_app:app --bind 0.0.0.0:$PORT` |

若误建成 **Static Site**，根目录没有 `index.html`，全站会返回纯文本 `Not Found`。  
Static Site 仅在 Publish Directory 设为 `web` 时可用；推荐仍用 Web Service。

部署成功后打开 `/healthz` 应返回 `{"ok": true, ...}`。
