# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from flask import Flask, Response, Request, request

app = Flask(__name__)


@app.route('/')
def home():
    return Response()