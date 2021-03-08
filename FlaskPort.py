#!/usr/bin/env python
from flask import Flask, request

app = Flask(__name__)


@app.route("/port")
def _port():
    return str(request.environ["REMOTE_PORT"]), {"Connection": "keep-alive"}


if __name__ == "__main__":
    app.run()
