#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: setup.py
Author: huxuan
Email: i(at)huxuan.org
Description: Python packaging for iptvtools.
"""
from setuptools import find_packages
from setuptools import setup

from iptvtools import __version__

DESCRIPTION = (
    'A set of scripts that help to better IPTV experience.'
)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Utilities'
]

INSTALL_REQUIRES = [
    'requests',
    'tqdm'
]

DEV_REQUIRES = [
    'pycodestyle',
    'pyflakes',
    'pylint'
]

EXTRAS_REQUIRE = {
    'dev': DEV_REQUIRES
}


def readme():
    """Parse README for long_description."""
    with open('README.md') as fin:
        return fin.read()


setup(name='iptvtools',
      version=__version__,
      description=DESCRIPTION,
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=CLASSIFIERS,
      keywords='iptv m3u playlist tools filter',
      url='https://github.com/huxuan/iptvtools',
      author='Xuan (Sean) Hu',
      author_email='i@huxuan.org',
      license='MIT',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      python_requires='>=3',
      entry_points={
          'console_scripts': [
              'iptv-filter=iptvtools.iptv_filter:main'
          ],
      },
      include_package_data=True)
