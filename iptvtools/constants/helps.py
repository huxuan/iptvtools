#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: constants.py
Author: huxuan
Email: i(at)huxuan.org
Description: Helps for iptvtools.
"""
from . import defaults

CONFIG = (
    f'Configuration file with title and id filter information, defaults to '
    f'`{defaults.CONFIG}`'
)
INPUT = (
    f'Valid M3U playlists, which could be a file or url, defaults to '
    f'`{defaults.INPUT}`.'
)
MIN_HEIGHT = (
    f'Minimal acceptable height/resolution, defaults to '
    f'{defaults.MIN_HEIGHT} which means {defaults.MIN_HEIGHT}P.'
)
OUTPUT = f'Output file name, defaults to `{defaults.OUTPUT}`.'
TEMPLATE = f'Template file name, defaults to `{defaults.TEMPLATE}`.'
TIMEOUT = (
    f'Acceptable timeout when retrieving stream information, defaults to '
    f'{defaults.TIMEOUT}.'
)
UDPXY = (
    f'UDP Proxy which will convert the url automatically, defaults to '
    f'`{defaults.UDPXY}`.'
)
