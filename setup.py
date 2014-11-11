#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from git_qdiff import VERSION

with open('README.md') as f:
    long_description = f.read()

setup(
    name='git-qdiff',
    version=VERSION,
    author='Fabien Meghazi',
    author_email='agr@amigrave.com',
    license='MIT',
    description="Bzr tool's qdiff for git",
    long_description=long_description,
    keywords='git qdiff bzr diff',
    url='https://github.com/amigrave/git-qdiff',
    py_modules=['git_qdiff'],
    scripts=['git-qdiff'],
)
