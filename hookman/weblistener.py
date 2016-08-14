# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from flask import Flask, Response, Request, request

app = Flask(__name__)
# app.debug = True

@app.route('/', methods=['POST'])
def home():
    event = request.headers.get('X-GitHub-Event', 'ping')
    if event == 'ping':
        return Response('pong')
    if event == 'push':
        return Response('hookman-0.1.0 get')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3610)