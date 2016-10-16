# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, jsonify

from py_atomist.swagger import spec

__version__ = '0.1.0'
__all__ = ['create_app']


def create_app():
    """
    Create the :class:`flask.app.Flask` app, as well as its models.
    Also, register blueprints.
    """
    app = Flask(__name__)

    from py_atomist.views import main_app
    app.register_blueprint(main_app)

    from py_atomist.tester.views import tester_app
    app.register_blueprint(tester_app)

    return app

