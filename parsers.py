#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: parser.py
Author: huxuan
Email: i(at)huxuan.org
Description: Simplified parser for m3u8 file.
"""
from urllib.request import urlopen
import os.path

from patterns import Patterns


def parse_content_to_lines(content):
    if os.path.isfile(content):
        return _parse_from_file(content)
    return _parse_from_url(content)


def parse_tag_inf(line):
    match = Patterns.EXTINF.fullmatch(line)
    return _transform_match_result(match)


def parse_tag_m3u(line):
    match = Patterns.EXTM3U.fullmatch(line)
    return _transform_match_result(match)


def _parse_from_file(filename):
    with open(filename, encoding='utf-8') as fin:
        return fin.read().splitlines()


def _parse_from_url(url):
    print(f'Retrieving playlists from {url}')
    with urlopen(url) as response:
        return response.read().decode('utf-8').splitlines()


def _transform_match_result(match):
    res = match.groupdict()
    if res.get('params'):
        res['params'] = dict(Patterns.PARAMS.findall(res['params']))
    return res
