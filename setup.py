#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'tatsu>=4.3',
    'matplotlib>=2.2'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Romain Picard",
    author_email='romain.picard@oakbits.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    description="A marble diagram generator",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='dooble',
    name='dooble',
    packages=find_packages(include=['dooble']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mainro/dooble',
    version='0.3.0',
    zip_safe=False,
    entry_points={
        'console_scripts': ['dooble=dooble.cli:main'],
    }
)
