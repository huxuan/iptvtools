#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: utils.py
Author: huxuan
Email: i(at)huxuan.org
Description: Relevant Utilities.
"""
from json import JSONDecodeError
from subprocess import PIPE
from subprocess import Popen
from subprocess import TimeoutExpired
import json

PROBE_COMMAND = (
    'ffprobe -hide_banner -show_streams -select_streams v '
    '-of json=c=1 -v quiet'
)


def probe(url, timeout=None):
    outs = None
    proc = Popen(f'{PROBE_COMMAND} {url}'.split(), stdout=PIPE, stderr=PIPE)
    try:
        outs, dummy = proc.communicate(timeout=timeout)
    except TimeoutExpired:
        proc.kill()
    if outs:
        try:
            return json.loads(outs.decode('utf-8'))
        except JSONDecodeError as exc:
            print(exc)
    return None


def max_height(stream_info):
    if stream_info.get('streams'):
        return max([
            stream.get('height', 0)
            for stream in stream_info['streams']
        ])
    return 0
