#!/usr/bin/env python3
"""tool15：深基课教程站（静态章节页）。"""

from __future__ import annotations

from pathlib import Path

from flask import Flask, abort, send_from_directory

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"

app = Flask(__name__)


@app.get("/")
def index():
    return send_from_directory(WEB, "index.html")


@app.get("/<path:path>")
def pages(path: str):
    target = (WEB / path).resolve()
    if not str(target).startswith(str(WEB.resolve())):
        abort(404)
    if target.is_dir():
        index_file = target / "index.html"
        if index_file.is_file():
            return send_from_directory(target, "index.html")
        abort(404)
    if not target.is_file():
        abort(404)
    return send_from_directory(target.parent, target.name)


def main() -> None:
    import os

    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5093"))
    print(f"tool15 深基课 → http://{host}:{port}")
    app.run(host=host, port=port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
