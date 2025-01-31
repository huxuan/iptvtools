#!/usr/bin/env python
"""Simplified parser for m3u8 file.

File: parser.py
Author: huxuan
Email: i(at)huxuan.org
"""

import os.path
import re
import tempfile
from collections.abc import Iterator
from typing import Any

import requests

from iptvtools.constants import patterns


def parse_content_to_lines(content: str, timeout: int | None = None) -> Iterator[str]:
    """Universal interface to split content into lines."""
    if os.path.isfile(content):
        with open(content, encoding="utf-8") as fp:
            for line in fp:
                yield re.sub(r"[^\S ]+", "", line.strip())
    else:
        with tempfile.TemporaryFile(mode="w+t") as fp:
            fp.write(requests.get(content, timeout=timeout).text)
            fp.seek(0)
            for line in fp:
                yield re.sub(r"[^\S ]+", "", line.strip())


def parse_tag_inf(line: str) -> dict[str, Any]:
    """Parse INF content."""
    match = patterns.EXTINF.fullmatch(line)
    res = match and match.groupdict() or {}
    if "params" in res:
        res["params"] = dict(patterns.PARAMS.findall(res["params"]))
    return res


def parse_tag_m3u(line: str) -> dict[str, Any]:
    """Parse M3U content."""
    match = patterns.EXTM3U.fullmatch(line)
    return match and match.groupdict() or {}
