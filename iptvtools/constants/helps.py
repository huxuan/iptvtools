#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helps for iptvtools.

File: constants.py
Author: huxuan
Email: i(at)huxuan.org
"""
CONFIG = (
    'Configuration file to unify title and id.'
)
CHANNEL_EXCLUDE = (
    'Channels to exclude with regex. '
    'Note: Blacklist has higher priority than whitelist.'
)
CHANNEL_INCLUDE = (
    'Channels to include with regex. '
    'Note: Only channels in the whitelist will be included if set.'
)
GROUP_EXCLUDE = (
    'Groups to exclude with regex.'
    'Note: Blacklist has higher priority than whitelist.'
)
GROUP_INCLUDE = (
    'Groups to include with regex.'
    'Note: Only groups in the whitelist will be included if set.'
)
INPUTS = (
    'One or more input m3u playlist files/urls.'
)
INTERVAL = (
    'Interval in seconds between successive fetching requests.'
)
LOG_LEVEL = 'Log level.'
MIN_HEIGHT = (
    'Minimum height/resolution to accept, 0 means no resolution filtering.'
)
OUTPUT = 'Output file name.'
REPLACE_GROUP_BY_SOURCE = (
    'Flag to replace the group title with the source name, where the source '
    'name is the basename of input files/urls without extension.'
)
RESOLUTION_ON_TITLE = (
    'Flag to append resolution such as 8K, 4K, 1080p, 720p to the title.'
)
SORT_KEYS = (
    'List of keys to sort the channels. Valid options currently supported '
    'are `group-title`, `tvg-id`, `height` and `title`.'
)
TEMPLATES = (
    'Template m3u files/urls with well-maintained channel information to '
    'replace the matched entries.'
)
TIMEOUT = (
    'Timeout threshold for fetching request.'
)
UDPXY = (
    'UDP Proxy for certain IPTV channels.'
)
