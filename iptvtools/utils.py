#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: utils.py
Author: huxuan
Email: i(at)huxuan.org
Description: Relevant Utilities.
"""
from subprocess import PIPE
from subprocess import Popen
from subprocess import TimeoutExpired
from urllib.parse import urlparse
import json

from .config import Config

PROBE_COMMAND = (
    'ffprobe -hide_banner -show_streams -select_streams v '
    '-of json=c=1 -v quiet'
)


def convert_url_with_udpxy(orig_url, udpxy):
    """Convert url with udpxy."""
    orig_url = orig_url.replace('///', '//')  # Hack to some abnormal urls.
    parsed_url = urlparse(orig_url)
    new_url = f'{udpxy}/{parsed_url.scheme}/{parsed_url.netloc}'
    return new_url


def filter_title_and_id(item):
    """Filter title and id."""
    for title_filter in sorted(Config().title_filters):
        if title_filter in item['title']:
            item['title'] = item['title'].replace(
                title_filter,
                Config().title_filters[title_filter])

    if 'tvg-name' in item.get('params'):
        item['id'] = item['params']['tvg-name']
    else:
        item['id'] = item['title']

    for id_filter in sorted(Config().id_filters):
        if id_filter in item['id']:
            item['id'] = item['id'].replace(
                id_filter,
                Config().id_filters[id_filter])

    return item


def max_height(stream_info):
    """Get max height from stream information."""
    if stream_info.get('streams'):
        return max([
            stream.get('height', 0)
            for stream in stream_info['streams']
        ])
    return 0


def probe(url, timeout=None):
    """Invoke probe to get stream information."""
    outs = None
    proc = Popen(f'{PROBE_COMMAND} {url}'.split(), stdout=PIPE, stderr=PIPE)
    try:
        outs, dummy = proc.communicate(timeout=timeout)
    except TimeoutExpired:
        proc.kill()
    if outs:
        try:
            return json.loads(outs.decode('utf-8'))
        except json.JSONDecodeError as exc:
            print(exc)
    return None
