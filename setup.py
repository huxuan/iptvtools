#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python packaging for iptvtools.

File: setup.py
Author: huxuan
Email: i(at)huxuan.org
"""
from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution
from setuptools import find_packages
from setuptools import setup


NAME = 'iptvtools'
AUTHOR = 'huxuan'
EMAIL = f'i+{NAME}@huxuan.org'

DESCRIPTION = (
    'A set of scripts that help to better IPTV experience.'
)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Utilities',
]

INSTALL_REQUIRES = [
    'requests',
    'tqdm',
]

KEYWORDS = [
    'iptv',
    'm3u',
    'playlist',
    'tools',
    'filter',
]

try:
    VERSION = f'v{get_distribution(NAME).version}'
except DistributionNotFound:
    VERSION = 'master'

PROJECT_URL = f'https://github.com/{AUTHOR}/{NAME}'
BASE_URL = f'{PROJECT_URL}/blob/{VERSION}'


def readme():
    """Parse README for long_description."""
    content = open('README.md').read()
    content = content.replace('README.md', f'{BASE_URL}/README.md', 1)
    content = content.replace('README-en.md', f'{BASE_URL}/README-en.md', 1)
    content = content.replace('README-zh.md', f'{BASE_URL}/README-zh.md', 1)
    return content


setup(name=NAME,
      description=DESCRIPTION,
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=CLASSIFIERS,
      keywords=' '.join(KEYWORDS),
      url=PROJECT_URL,
      author=AUTHOR,
      author_email=EMAIL,
      license='MIT',
      packages=find_packages(exclude=['tests']),
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      install_requires=INSTALL_REQUIRES,
      python_requires='>=3',
      entry_points={
          'console_scripts': [
              'iptv-filter=iptvtools.iptv_filter:main',
          ],
      },
      include_package_data=True)
