# -*- coding:utf-8 -*-

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def headers():
    return '<br/>'.join(['%s => %s' % (key, value) for (key, value) in request.headers.items()])


if __name__ == "__main__":
    app.run()

