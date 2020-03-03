#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Relevant Utilities.

File: utils.py
Author: huxuan
Email: i(at)huxuan.org
"""
import json
import socket
import struct
from subprocess import PIPE
from subprocess import Popen
from subprocess import TimeoutExpired
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


def check_stream(url, args):
    """Check stream information."""
    stream_info = probe(url, args.timeout)
    if stream_info:
        if max_height(stream_info) >= args.min_height:
            return True
    return False


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
    mreq = struct.pack("4sl", socket.inet_aton(ipaddr), socket.INADDR_ANY)
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
