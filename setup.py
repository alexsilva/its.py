# -*- coding: utf-8 -*-
"""
is.py
~~~~~

This simple module gives you a set of Python runtime environment flags.

"""

from setuptools import setup

setup(
    name='its',
    version='1.0.0',
    url='https://github.com/kennethreitz/its',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description=' Python runtime environment flags.',
    long_description=__doc__,
    py_modules=['its'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
