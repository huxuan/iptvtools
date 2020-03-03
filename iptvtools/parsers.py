#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simplified parser for m3u8 file.

File: parser.py
Author: huxuan
Email: i(at)huxuan.org
"""
import os.path
from urllib.request import urlopen

from iptvtools.constants import patterns


def parse_content_to_lines(content):
    """Universal interface to split content into lines."""
    if os.path.isfile(content):
        return _parse_from_file(content)
    return _parse_from_url(content)


def parse_tag_inf(line):
    """Parse INF content."""
    match = patterns.EXTINF.fullmatch(line)
    res = match.groupdict()
    if 'params' in res:
        res['params'] = dict(patterns.PARAMS.findall(res['params']))
    return res


def parse_tag_m3u(line):
    """Parse M3U content."""
    match = patterns.EXTM3U.fullmatch(line)
    return match.groupdict()


def _parse_from_file(filename):
    """Parse content from file."""
    print(f'Retrieving playlists from file: {filename}')
    with open(filename, encoding='utf-8') as fin:
        return fin.read().splitlines()


def _parse_from_url(url):
    """Parse content from url."""
    print(f'Retrieving playlists from url: {url}')
    with urlopen(url) as response:
        return response.read().decode('utf-8').splitlines()
