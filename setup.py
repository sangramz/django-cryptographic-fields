#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from setuptools import setup


with open('cryptographic_fields/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-cryptographic-fields',
    version=version,
    packages=['cryptographic_fields'],
    license='MIT License',
    include_package_data=True,
    description=(
        'A set of django fields that internally are encrypted using the '
        'cryptography.io native python encryption library.'
    ),
    long_description=README,
    url='http://github.com/foundertherapy/django-cryptographic-fields/',
    author='Dana Spiegel',
    author_email='dana@foundertherapy.co',
    install_requires=[
        'Django>=1.7',
        'cryptography>=0.8.2',
    ],
)
