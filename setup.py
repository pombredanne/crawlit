#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from crawlit import get_version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

install_requires = open('requirements.txt').readlines()

setup(
    name='crawlit',
    version=get_version(),
    description='Python web crawler with limitations.',
    long_description=readme + '\n\n' + history,
    author='kracekumar',
    author_email='me@kracekumar.com',
    url='https://github.com/kracekumar/crawlit',
    packages=[
        'crawlit',
    ],
    package_dir={'crawlit': 'crawlit'},
    include_package_data=True,
    install_requires=install_requires,
    license="BSD",
    zip_safe=False,
    keywords='crawlit',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'crawlit = crawlit.crawlit:main',
        ]
    }
)
