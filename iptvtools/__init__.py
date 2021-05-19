#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Init for iptvtools.

File: __init__.py
Author: huxuan
Email: i(at)huxuan.org
"""
from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution


__version__ = '0.0.0'
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
