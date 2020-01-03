#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: models.py
Author: huxuan
Email: i(at)huxuan.org
Description: Playlist which contains all the channels' information.
"""
import sys

from tqdm import tqdm

from . import parsers
from . import utils
from .constants import tags


class Playlist():
    """Playlist model."""
    def __init__(self):
        self.data = {}
        self.template = {}
        self.tvg_url = None

    def __str__(self):
        res = []
        res.append(tags.M3U)
        if self.tvg_url is not None:
            res[0] += f' x-tvg-url="{self.tvg_url}"'
        urls = sorted(self.data, key=self.__sort_by_tvg_id_and_title)
        for url in urls:
            internal_id = self.data[url]['id']
            if internal_id in self.template.keys():
                entry = self.template[internal_id]
            else:
                entry = self.data[url]
            params_dict = entry.get('params', {})
            params = ' '.join([f'{key}="{value}"'
                               for key, value in params_dict.items()])
            res.append(
                f'{tags.INF}:{entry["duration"]} {params},{entry["title"]}'
            )
            res.append(url)
        return '\n'.join(res)

    def parse(self, content, udpxy=None, is_template=False):
        """Parse content."""
        lines = parsers.parse_content_to_lines(content)

        if lines[0].startswith(tags.M3U):
            res = parsers.parse_tag_m3u(lines[0])
            if res.get('tvg-url'):
                self.tvg_url = res.get('tvg-url')
            lines = lines[1:]

        current_item = {}
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith(tags.INF):
                current_item = parsers.parse_tag_inf(line)
                current_item = utils.filter_title_and_id(current_item)
            else:
                if is_template:
                    self.template[current_item['id']] = current_item
                else:
                    if udpxy:
                        line = utils.convert_url_with_udpxy(line, udpxy)
                    self.data[line] = current_item

    def filter(self, min_height=None, timeout=None):
        """Filter process."""
        if min_height:
            urls = list(self.data.keys())
            for url in tqdm(urls, ascii=True):
                stream_info = utils.probe(url, timeout)
                if stream_info:
                    if utils.max_height(stream_info) < min_height:
                        self.data.pop(url)
                else:
                    self.data.pop(url)

    def __sort_by_tvg_id_and_title(self, url):
        """Sort by tvg-id and title."""
        internal_id = self.data[url]['id']
        tvg_id = sys.maxsize
        title = self.data[url]['title']
        if internal_id in self.template.keys():
            tvg_id = int(self.template[internal_id]['params']['tvg-id'])
            title = self.template[internal_id]['title']
        return tvg_id, title

    def __sort_by_data_title(self, url):
        """Sort by title in data."""
        return self.data[url]['title']
