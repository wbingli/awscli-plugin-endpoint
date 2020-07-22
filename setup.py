#!/usr/bin/env python
import sys
from setuptools import setup

requires = ['awscli>=1.11.0']

setup(
    name='awscli-plugin-endpoint',
    packages=['awscli_plugin_endpoint'],
    version='0.4',
    description='Endpoint plugin for AWS CLI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Wenbing Li',
    author_email='wbingli@gmail.com',
    url='https://github.com/wbingli/awscli-plugin-endpoint',
    download_url='https://github.com/wbingli/awscli-plugin-endpoint/tarball/0.4',
    keywords=['awscli', 'plugin', 'endpoint'],
    install_requires=requires,
    classifiers = []
)
