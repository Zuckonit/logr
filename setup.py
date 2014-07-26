#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import logr

setup(
    name = 'logr',
    version = logr.__version__,
    zip_safe=False,
    author=logr.__author__,
    author_email='Zuckerwooo@gmail.com',
    license='MIT',
    platforms=['any'],
    packages = ['logr'],
    keywords='logging',
    url='https://github.com/zuckonit/logr',
    description='simple logging wrapper',
    long_description="""
        use logging like print hello world
    """,
)
