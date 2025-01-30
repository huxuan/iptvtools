#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Patterns for iptvtools.

File: constants.py
Author: huxuan
Email: i(at)huxuan.org
"""
import re


PARAMS = re.compile(r'(\S+)="(.*?)"')
EXTINF = re.compile(
    r'^#EXTINF:(?P<duration>-?\d+?) ?(?P<params>.*),(?P<title>.*?)$')
EXTM3U = re.compile(r'^#EXTM3U ?(?P<params>.*)$')
