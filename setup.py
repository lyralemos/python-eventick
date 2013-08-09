#!/usr/bin/env python

from distutils.core import setup

setup(name='python-eventick',
      version='0.1',
      description='Python Eventick Library',
      long_description=open("README.md").read(),
      classifiers=[
        "Programming Language :: Python",
      ],
      license='GPLv2',
      author='Alexandre Marinho',
      author_email='alexandre.marinho@nti.ufal.br',
      url='http://www.github.com/lyralemos/python-eventick',
      packages=['eventick'],
      install_requires=['requests'],
     )
