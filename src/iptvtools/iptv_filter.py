#!/usr/bin/env python
"""Filter IPTV m3u playlists according to customized criteria.

File: main.py
Author: huxuan
Email: i(at)huxuan.org
"""

import argparse
import logging
import shutil

from iptvtools import __version__, exceptions
from iptvtools.config import Config
from iptvtools.constants import defaults, helps
from iptvtools.models import Playlist


def parse_args():
    """Arguments Parsers."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--channel-exclude", help=helps.CHANNEL_EXCLUDE)
    parser.add_argument("--channel-include", help=helps.CHANNEL_INCLUDE)
    parser.add_argument("--group-exclude", help=helps.GROUP_EXCLUDE)
    parser.add_argument("--group-include", help=helps.GROUP_INCLUDE)
    parser.add_argument(
        "--max-height", default=defaults.MAX_HEIGHT, type=int, help=helps.MAX_HEIGHT
    )
    parser.add_argument(
        "--min-height", default=defaults.MIN_HEIGHT, type=int, help=helps.MIN_HEIGHT
    )
    parser.add_argument("-c", "--config", default=defaults.CONFIG, help=helps.CONFIG)
    parser.add_argument(
        "-i", "--inputs", nargs="*", default=defaults.INPUTS, help=helps.INPUTS
    )
    parser.add_argument(
        "-I", "--interval", default=defaults.INTERVAL, type=int, help=helps.INTERVAL
    )
    parser.add_argument(
        "-L", "--log-level", default=defaults.LOG_LEVEL, help=helps.LOG_LEVEL
    )
    parser.add_argument(
        "-n",
        "--skip-connectivity-check",
        action="store_true",
        help=helps.SKIP_CONNECTIVITY_CHECK,
    )
    parser.add_argument("-o", "--output", default=defaults.OUTPUT, help=helps.OUTPUT)
    parser.add_argument(
        "-r",
        "--replace-group-by-source",
        action="store_true",
        help=helps.REPLACE_GROUP_BY_SOURCE,
    )
    parser.add_argument(
        "-R",
        "--resolution-on-title",
        action="store_true",
        help=helps.RESOLUTION_ON_TITLE,
    )
    parser.add_argument(
        "-s", "--sort-keys", nargs="*", default=defaults.SORT_KEYS, help=helps.SORT_KEYS
    )
    parser.add_argument(
        "-t", "--templates", nargs="*", default=defaults.TEMPLATES, help=helps.TEMPLATES
    )
    parser.add_argument(
        "-T", "--timeout", default=defaults.TIMEOUT, type=int, help=helps.TIMEOUT
    )
    parser.add_argument("-u", "--udpxy", default=defaults.UDPXY, help=helps.UDPXY)
    parser.add_argument("-v", "--version", action="version", version=__version__)
    return parser.parse_args()


def main():
    """Filter m3u playlists."""
    args = parse_args()

    logging.basicConfig(level=args.log_level.upper())

    if args.max_height or args.min_height or args.resolution_on_title:
        if shutil.which("ffprobe") is None:
            raise exceptions.FFmpegNotInstalledError()

    Config.init(args.config)
    playlist = Playlist(args)
    playlist.parse()
    playlist.filter()
    playlist.export()
    if playlist.inaccessible_urls:
        logging.info("Inaccessible Urls:")
        logging.info("\n".join(sorted(playlist.inaccessible_urls)))
    if playlist.low_res_urls:
        logging.info("Low resolution Urls:")
        logging.info("\n".join(sorted(playlist.low_res_urls)))
    if playlist.high_res_urls:
        logging.info("High resolution Urls:")
        logging.info("\n".join(sorted(playlist.high_res_urls)))


if __name__ == "__main__":
    main()
