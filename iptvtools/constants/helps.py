#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helps for iptvtools.

File: constants.py
Author: huxuan
Email: i(at)huxuan.org
"""
CONFIG = (
    f'Configuration file to unify title and id.'
)
INPUTS = (
    f'One or more input m3u playlist files/urls.'
)
INTERVAL = (
    f'Interval in seconds between successive fetching requests.'
)
MIN_HEIGHT = (
    f'Minimum height/resolution to accept, 0 means no resolution filtering.'
)
OUTPUT = f'Output file name.'
REPLACE_GROUP_BY_SOURCE = (
    f'Flag to replace the group title with the source name, where the source '
    f'name is the basename of input files/urls without extension.'
)
RESOLUTION_ON_TITLE = (
    f'Flag to append resolution such as 8K, 4K, 1080p, 720p to the title.'
)
SORT_KEYS = (
    f'List of keys to sort the channels. Valid options currently supported '
    f'are `tvg-id`, `height` and `title`.'
)
TEMPLATES = (
    f'Template m3u files/urls with well-maintained channel information to '
    f'replace the matched entries.'
)
TIMEOUT = (
    f'Timeout threshold for fetching request.'
)
UDPXY = (
    f'UDP Proxy for certain IPTV channels.'
)
