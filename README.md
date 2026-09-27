# AI_Supervision

深基课教程站（Flask 静态章节）：Python → 数据计算 → 机器学习直觉 → PyTorch → 小项目 → AI 工具 → 创新点流程 → 论文写作。

## 本地运行

```bash
pip install -r requirements.txt
python web_app.py
```

浏览器打开 http://127.0.0.1:5093

## Render 部署

- Build: `pip install -r requirements.txt`
- Start: `gunicorn web_app:app --bind 0.0.0.0:$PORT`

也可使用仓库根目录的 `render.yaml`（Blueprint）。
