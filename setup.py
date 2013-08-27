#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='python-eventick',
      version='0.2',
      description='Python Eventick Library',
      long_description=open("README.md").read(),
      classifiers=[
        "Programming Language :: Python",
      ],
      license='GPLv2',
      author='Alexandre Marinho',
      author_email='alexandre.marinho@nti.ufal.br',
      url='http://www.github.com/lyralemos/python-eventick',
      packages=find_packages(),
      package_data = {
        '': ['README.md']
      },
      include_package_data=True,
      zip_safe=False,
      install_requires=['requests'],
     )
