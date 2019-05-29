#! /usr/bin/env python
# ! coding=utf-8


from setuptools import setup
from .sunow import __VERSION__

setup(name='sunow',
      version=__VERSION__,
      description='Some packages in common use',
      author='Sunow Yang',
      author_email='sunow_yang@outlook.com',
      url=' https://github.com/sunowYang/sunow',
      packages=['sunow'],
      long_description="Think about the ideal way to write a web app. Write the code to make it happen.",
      license="Public domain",
      platforms=["3.7"], install_requires=['xlrd', 'xlwt', 'xlutils']
      )
