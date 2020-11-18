# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in healthcorner/__init__.py
from healthcorner import __version__ as version

setup(
	name='healthcorner',
	version=version,
	description='health corner crm',
	author='yazan',
	author_email='yazansorour1@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
