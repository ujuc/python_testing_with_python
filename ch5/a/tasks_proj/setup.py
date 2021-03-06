#!/usr/bin/evn python

from setuptools import setup, find_packages
import pkg_resources

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tasks',
    version=pkg_resources.require('tasks')[0].version,
    author='Thomas ujuc',
    author_email='sungjin.kang@ujuc.me',
    description='Pytest example Task App',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # packages=find_packages(),
    packages=['tasks'],
    package_dir={'tasks': 'src/tasks'},
    install_requires=[
        'pytest', 'tinydb', 'pymongo',
    ],
)
