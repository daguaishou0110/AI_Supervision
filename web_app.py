#!/usr/bin/env python3
"""tool15：深基课教程站（静态章节页）。"""

from __future__ import annotations

import os
from pathlib import Path

from flask import Flask, abort, jsonify, send_from_directory

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"

app = Flask(__name__)


@app.get("/healthz")
def healthz():
    return jsonify(
        ok=True,
        web_dir=str(WEB),
        index_exists=(WEB / "index.html").is_file(),
    )


@app.get("/")
def index():
    index_file = WEB / "index.html"
    if not index_file.is_file():
        abort(500, description=f"missing index at {index_file}")
    return send_from_directory(WEB, "index.html")


@app.get("/<path:path>")
def pages(path: str):
    web_root = WEB.resolve()
    target = (WEB / path).resolve()
    try:
        target.relative_to(web_root)
    except ValueError:
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
    # Render / PaaS always sets PORT — bind all interfaces so the proxy can reach us.
    port = int(os.environ.get("PORT", "5093"))
    host = os.environ.get("HOST") or ("0.0.0.0" if "PORT" in os.environ else "127.0.0.1")
    print(f"tool15 深基课 → http://{host}:{port} (WEB={WEB})")
    app.run(host=host, port=port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
