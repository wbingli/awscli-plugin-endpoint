#!/usr/bin/env python
import sys
from setuptools import setup

requires = ['awscli>=1.11.0']

setup(
    name='awscli-plugin-endpoint',
    version='0.1',
    description='Endpoint plugin for AWS CLI',
    long_description=open('README.md').read(),
    author='Bruce Li',
    author_email='wbinglee@gmail.com',
    url='https://github.com/wbinglee/awscli_plugin_endpoint',
    packages=['awscli_plugin_endpoint'],
    install_requires=requires,
    classifiers = []
)
