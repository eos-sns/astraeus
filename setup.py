# !/usr/bin/python3
# -*- coding: utf-8 -*-


""" Install dependencies """

from setuptools import setup, find_packages

PACKAGE_NAME = 'Astraeus'
LITTLE_DESCRIPTION = 'Saves stuff in memcache'
DESCRIPTION = '{}: {}'.format(PACKAGE_NAME, LITTLE_DESCRIPTION)

setup(
    name=PACKAGE_NAME,
    version="1.0",
    description=LITTLE_DESCRIPTION,
    long_description=DESCRIPTION,
    keywords="eos",
    url="https://github.com/eos-sns/astraeus",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        'pymemcache'
    ]
)
