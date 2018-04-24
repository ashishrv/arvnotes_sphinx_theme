#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io

from setuptools import setup
from setuptools import find_packages

# README into long description
with io.open('README.md', encoding='utf-8') as readme_file:
    long_description = readme_file.read()


setup(
    name='arvnotes-sphinx-theme',
    # Version is date based as year.month[.serial], where serial is used
    # if multiple releases are needed to address build failures.
    version='2018.4',
    description='Sphinx theme for maintaining notes',
    long_description=long_description,
    author='Ashish RV',
    author_email='ashish.vid@gmail.com',
    url='https://docs.python.org',
    packages=['arvnotes_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'sphinx.html_themes': [
            'arvnotes_sphinx_theme = arvnotes_sphinx_theme',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
