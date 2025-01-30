#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simplified parser for m3u8 file.

File: parser.py
Author: huxuan
Email: i(at)huxuan.org
"""
import os.path
import re
import tempfile

import requests

from iptvtools.constants import patterns


def parse_content_to_lines(content):
    """Universal interface to split content into lines."""
    if os.path.isfile(content):
        fp = open(content, encoding='utf-8')
    else:
        fp = tempfile.TemporaryFile(mode='w+t')
        fp.write(requests.get(content).text)
        fp.seek(0)
    for line in fp:
        yield re.sub(r'[^\S ]+', '', line.strip())
    fp.close()


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
