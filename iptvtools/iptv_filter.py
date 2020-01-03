#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: main.py
Author: huxuan
Email: i(at)huxuan.org
Description: Filter IPTV m3u playlists according to customized criteria.
"""
import argparse

from . import __version__
from .config import Config
from .constants import defaults
from .constants import helps
from .models import Playlist


def parse_args():
    """Arguments Parsers."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--min-height', default=defaults.MIN_HEIGHT, type=int,
                        help=helps.MIN_HEIGHT)
    parser.add_argument('-c', '--config', default=defaults.CONFIG,
                        help=helps.CONFIG)
    parser.add_argument('-i', '--input', action='append',
                        default=[], help=helps.INPUT)
    parser.add_argument('-o', '--output', default=defaults.OUTPUT,
                        help=helps.OUTPUT)
    parser.add_argument('-t', '--template', action='append',
                        default=[], help=helps.TEMPLATE)
    parser.add_argument('-T', '--timeout', default=defaults.TIMEOUT, type=int,
                        help=helps.TIMEOUT)
    parser.add_argument('-u', '--udpxy', default=defaults.UDPXY,
                        help=helps.UDPXY)
    parser.add_argument('-v', '--version', action='version',
                        version=__version__)
    return parser.parse_args()


def main():
    """Main process."""
    args = parse_args()
    if not args.input:
        args.input = [defaults.INPUT]
    Config.init(args.config)
    playlist = Playlist()
    playlist.parse(args.input, args.udpxy)
    playlist.parse(args.template, is_template=True)
    playlist.filter(args.min_height, args.timeout)
    print(f'{len(playlist.data)} channels after filtering!')
    open(args.output, 'w', encoding='utf-8').write(str(playlist))


if __name__ == '__main__':
    main()
