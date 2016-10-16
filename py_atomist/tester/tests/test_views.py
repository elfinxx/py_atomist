# -*- coding: utf-8 -*-
from flask import url_for


def test_tester_index(client):
    res = client.get(url_for('tester_app.index'))
    assert res.data == b'Hello World!'
