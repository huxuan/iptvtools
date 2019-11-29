#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: models.py
Author: huxuan
Email: i(at)huxuan.org
Description: Simplified M3U8 and other related models.
"""
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

from tqdm import tqdm

from iptv_m3u_filter import parsers
from iptv_m3u_filter import utils
from iptv_m3u_filter.tags import Tags


class M3U8():
    def __init__(self):
        self.data = {}
        self.tvg_url = None

    def __str__(self):
        res = []
        res.append(Tags.M3U)
        if self.tvg_url is not None:
            res[0] += f' x-tvg-url="{self.tvg_url}"'
        for url, entry in self.data.items():
            params_dict = entry.get('params', {})
            params = ' '.join([f'{key}="{value}"'
                               for key, value in params_dict.items()])
            res.append(
                f'{Tags.INF}:{entry["duration"]} {params},{entry["title"]}'
            )
            res.append(url)
        return '\n'.join(res)

    def parse(self, content):
        lines = parsers.parse_content_to_lines(content)

        if lines[0].startswith(Tags.M3U):
            res = parsers.parse_tag_m3u(lines[0])
            if res.get('tvg-url'):
                self.tvg_url = res.get('tvg-url')
            lines = lines[1:]

        current_item = {}
        for line in lines:
            if line.startswith(Tags.INF):
                current_item = parsers.parse_tag_inf(line)
            else:
                self.data[line] = current_item

    def filter(self, args):
        flag_stream = args.min_height > 0

        with ThreadPoolExecutor(max_workers=args.max_workers) as executor:
            if flag_stream:

                future_dict = {
                    executor.submit(utils.probe, url, args.timeout): url
                    for url in self.data}

                for future in tqdm(futures.as_completed(future_dict),
                                   total=len(self.data),
                                   ascii=True):
                    stream_info = future.result()
                    url = future_dict[future]
                    if stream_info:
                        if utils.max_height(stream_info) < args.min_height:
                            self.data.pop(url)
                    else:
                        self.data.pop(url)
