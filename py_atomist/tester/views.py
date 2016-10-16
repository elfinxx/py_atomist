# -*- coding: utf-8 -*-
from flask import Blueprint

__all__ = ['tester_app']

tester_app = Blueprint('tester_app', __name__)


@tester_app.route('/')
def index():
    return "Hello World!"
