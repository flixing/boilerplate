# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='boilerplate',
      py_modules=['boilerplate'],
      version='0.0.1',
      description='Default boilerplate for python projects',
      url='https://github.com/natanocr/boilerplate',
      author='Natan Oliveira',
      author_email='natanoliveiracruz@gmail.com',
      keywords='python boilerplate',
      long_description=open('README.rst').read(),
      license='MIT',
      platforms='OS Independent',
      packages=['boilerplate'],
      install_requires=[
            # 'package',
      ],
      test_suite='test',
      zip_safe=False)
