#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helps for iptvtools.

File: constants.py
Author: huxuan
Email: i(at)huxuan.org
"""
from iptvtools.constants import defaults

CONFIG = (
    f'Configuration file to unify title and id information, defaults to '
    f'`{defaults.CONFIG}`'
)
INPUT = (
    f'Input playlist file/url, defaults to `[{defaults.INPUT}]`. Note that '
    f'multiple input files/urls are supported.'
)
INTERVAL = (
    f'Interval in seconds between fetching each url, defaults to '
    f'{defaults.INTERVAL}.'
)
MIN_HEIGHT = (
    f'Minimal acceptable height/resolution, defaults to {defaults.MIN_HEIGHT}'
    f'which means {defaults.MIN_HEIGHT}P. Set 0 to disable the filtering.'
)
OUTPUT = f'Output playlist file name, defaults to `{defaults.OUTPUT}`.'
REPLACE_GROUP_BY_SOURCE = (
    f'Flag to indicate whether to replace the group title with source name, '
    f'where source name is the basename of input files/urls without extension.'
)
TEMPLATE = (
    f'Template playlist file/url which have well-maintained channel '
    f'information to cooperate with EPG and will replace the corresponding '
    f'entry (except url) if matched , defaults to `[]`. Note that multiple '
    f'template files/urls are supported.'
)
TIMEOUT = (
    f'Acceptable timeout when retrieving stream information, defaults to '
    f'{defaults.TIMEOUT}.'
)
UDPXY = (
    f'UDP Proxy which will convert the url automatically, defaults to '
    f'`{defaults.UDPXY}`.'
)
