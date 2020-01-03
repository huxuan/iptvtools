#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: constants.py
Author: huxuan
Email: i(at)huxuan.org
Description: Patterns for iptvtools.
"""
import re

PARAMS = re.compile(r'(\S+)="(.*?)"')
EXTINF = re.compile(
    r'^#EXTINF:(?P<duration>-?\d+?) ?(?P<params>.*),(?P<title>.*?)$')
EXTM3U = re.compile(r'^#EXTM3U ?(?P<params>.*)$')
