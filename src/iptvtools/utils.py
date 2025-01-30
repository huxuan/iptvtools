#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Relevant Utilities.

File: utils.py
Author: huxuan
Email: i(at)huxuan.org
"""
import json
import logging
import socket
import struct
from subprocess import PIPE  # noqa: S404
from subprocess import Popen  # noqa: S404
from subprocess import TimeoutExpired  # noqa: S404
from urllib.parse import urlparse

import requests

from iptvtools.config import Config


PROBE_COMMAND = (
    'ffprobe -hide_banner -show_streams -select_streams v '
    '-of json=c=1 -v quiet'
)

UDP_SCHEME = (
    'udp',
    'rtp',
)


def convert_url_with_udpxy(orig_url, udpxy):
    """Convert url with udpxy."""
    parsed_url = urlparse(orig_url)
    if parsed_url.scheme in UDP_SCHEME:
        return f'{udpxy}/{parsed_url.scheme}/{parsed_url.netloc}'
    return orig_url


def unify_title_and_id(item):
    """Unify title and id."""
    for title_unifier in sorted(Config.title_unifiers):
        if title_unifier in item['title']:
            item['title'] = item['title'].replace(
                title_unifier,
                Config.title_unifiers[title_unifier])

    if 'tvg-name' in item.get('params'):
        item['id'] = item['params']['tvg-name']
    else:
        item['id'] = item['title']

    for id_unifier in sorted(Config.id_unifiers):
        if id_unifier in item['id']:
            item['id'] = item['id'].replace(
                id_unifier,
                Config.id_unifiers[id_unifier])

    return item


def probe(url, timeout=None):
    """Invoke probe to get stream information."""
    outs = None
    with Popen(  # noqa: S603
            f'{PROBE_COMMAND} {url}'.split(),
            stdout=PIPE, stderr=PIPE) as proc:
        try:
            outs, _ = proc.communicate(timeout=timeout)
        except TimeoutExpired:
            proc.kill()
    if outs:
        try:
            return json.loads(outs.decode('utf-8'))
        except json.JSONDecodeError as exc:
            logging.error(exc)
    return None


def check_stream(url, timeout=None):
    """Check stream information and return height."""
    stream_info = probe(url, timeout)
    if stream_info and stream_info.get('streams'):
        return max([
            stream.get('height', 0)
            for stream in stream_info['streams']
        ])
    return 0


def check_connectivity(url, timeout=None):
    """Check connectivity."""
    parsed_url = urlparse(url)
    if parsed_url.scheme in UDP_SCHEME:
        return check_udp_connectivity(parsed_url.netloc, timeout)
    return check_http_connectivity(url, timeout)


def check_udp_connectivity(url, timeout=None):
    """Check UDP connectivity."""
    ipaddr, port = url.rsplit(':', 1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.bind(('', int(port)))
    mreq = struct.pack('4sl', socket.inet_aton(ipaddr), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    try:
        if sock.recv(10240):
            return True
    except socket.timeout:
        pass
    return False


def check_http_connectivity(url, timeout=None):
    """Check HTTP connectivity."""
    try:
        return requests.get(url, timeout=timeout, stream=True).ok
    except requests.RequestException:
        return False


def height_to_resolution(height):
    """Convert height to resolution."""
    if not height:
        return ''
    if height >= 4320:
        return '8K'
    if height >= 2160:
        return '4K'
    if height >= 1080:
        return '1080p'
    if height >= 720:
        return '720p'
    return f'{height}p'
