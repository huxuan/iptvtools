#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: main.py
Author: huxuan
Email: i(at)huxuan.org
Description: Main entrance for iptv-m3u-filer.
"""
import argparse

from defaults import Defaults
from helps import Helps
from models import M3U8


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min-height', default=Defaults.MIN_HEIGHT, type=int,
                        help=Helps.MIN_HEIGHT)
    parser.add_argument('-i', '--input', default=Defaults.INPUT,
                        help=Helps.INPUT)
    parser.add_argument('-o', '--output', default=Defaults.OUTPUT,
                        help=Helps.OUTPUT)
    parser.add_argument('-p', '--max-workers', default=Defaults.MAX_WORKERS,
                        type=int, help=Helps.MAX_WORKERS)
    parser.add_argument('-t', '--timeout', default=2, type=int,
                        help=Helps.TIMEOUT)
    return parser.parse_args()


def main():
    args = parse_args()
    m3u8 = M3U8()
    m3u8.parse(args.input)
    m3u8.filter(args)
    print(f'{len(m3u8.data)} channels after filtering!')
    open(args.output, 'w', encoding='utf-8').write(str(m3u8))


if __name__ == '__main__':
    main()
