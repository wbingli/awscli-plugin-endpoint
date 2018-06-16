#!/usr/bin/env python
import sys
from setuptools import setup

requires = ['awscli>=1.11.0']

setup(
    name='awscli-plugin-endpoint',
    packages=['awscli_plugin_endpoint'],
    version='0.3',
    description='Endpoint plugin for AWS CLI',
    long_description=open('README.md').read(),
    author='Wenbing Li',
    author_email='wbinglee@gmail.com',
    url='https://github.com/wbinglee/awscli-plugin-endpoint',
    download_url='https://github.com/wbinglee/awscli-plugin-endpoint/tarball/0.3',
    keywords=['awscli', 'plugin', 'endpoint'],
    install_requires=requires,
    classifiers = []
)
