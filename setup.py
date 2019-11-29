#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: setup.py
Author: huxuan
Email: i(at)huxuan.org
Description: Python packaging for iptv-m3u-filter.
"""
from setuptools import setup

DESCRIPTION = (
    'A script to filter IPTV m3u playlists according to customized criteria.'
)


def readme():
    with open('README.md') as fin:
        return fin.read()


setup(name='iptv_m3u_filter',
      version='0.1',
      description=DESCRIPTION,
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      keywords='iptv m3u playlist filter',
      url='https://github.com/huxuan/iptv-m3u-filter',
      author='Xuan (Sean) Hu',
      author_email='i@huxuan.org',
      license='MIT',
      packages=['iptv_m3u_filter'],
      install_requires=[
          'tqdm',
      ],
      entry_points={
          'console_scripts': ['iptv-m3u-filter=iptv_m3u_filter.main:main'],
      },
      include_package_data=True)
