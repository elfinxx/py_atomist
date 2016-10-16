# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from py_atomist import __version__


setup(
    name="py_atomist",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["py_atomist", "py_atomist.tester"],
    platforms=["any"]
)
