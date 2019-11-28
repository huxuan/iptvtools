#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: helps.py
Author: huxuan
Email: i(at)huxuan.org
Description: Help messages.
"""
from defaults import Defaults


class Helps:
    INPUT = (
        f'Valid M3U playlists, which could be a file or url, defaults to '
        f'`{Defaults.INPUT}`.'
    )
    MAX_WORKERS = (
        f'Number of threads to perform the filtering process, defaults to '
        f'{Defaults.MAX_WORKERS}.'
    )
    MIN_HEIGHT = (
        f'Minimal acceptable height/resolution, defaults to '
        f'{Defaults.MIN_HEIGHT} which means {Defaults.MIN_HEIGHT}P.'
    )
    OUTPUT = f'Output file name, defaults to `{Defaults.OUTPUT}`.'
    TIMEOUT = (
        f'Acceptable timeout when retrieving stream information, defaults to '
        f'{Defaults.TIMEOUT}.'
    )
