#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Playlist which contains all the channels' information.

File: models.py
Author: huxuan
Email: i(at)huxuan.org
"""
import os.path
import random
import sys
import time

from tqdm import tqdm

from iptvtools import parsers
from iptvtools import utils
from iptvtools.constants import tags


class Playlist():
    """Playlist model."""

    def __init__(self, args):
        """Init for Playlist."""
        self.args = args
        self.data = {}
        self.inaccessible_urls = set()
        self.poor_urls = set()
        self.tvg_url = None

    def export(self):
        """Export playlist information."""
        res = []
        res.append(tags.M3U)
        if self.tvg_url is not None:
            res[0] += f' x-tvg-url="{self.tvg_url}"'
        for internal_id in self.data:

            url = self.data[internal_id]['url']
            if url in self.inaccessible_urls or url in self.poor_urls:
                continue

            entry = self.data[internal_id]
            params_dict = entry.get('params', {})
            if self.args.replace_group_by_source:
                params_dict['group-title'] = self.data[internal_id]['source']
            params = ' '.join([f'{key}="{value}"'
                               for key, value in params_dict.items()])
            duration = entry['duration']
            title = entry['title']
            if self.args.resolution_on_title:
                height = self.data[internal_id]['height']
                title += f' [{utils.height_to_resolution(height)}]'

            res.append(
                f'{tags.INF}:{duration} {params},{title}\n{url}')

        open(self.args.output, 'w', encoding='utf-8').write('\n'.join(res))

    def parse(self):
        """Parse contents."""
        self._parse(self.args.inputs, udpxy=self.args.udpxy)
        self._parse(self.args.templates, is_template=True)

    def _parse(self, sources, udpxy=None, is_template=False):
        """Parse playlist sources."""
        for source in sources:
            lines = parsers.parse_content_to_lines(source)
            source_name = os.path.splitext(os.path.basename(source))[0]

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
                    current_item = utils.unify_title_and_id(current_item)
                    current_id = current_item['id']
                else:
                    if is_template:
                        if current_id not in self.data:
                            continue
                        current_params = current_item['params']
                        self.data[current_id]['params'].update(current_params)
                        self.data[current_id]['title'] = current_item['title']
                    else:
                        if udpxy:
                            line = utils.convert_url_with_udpxy(line, udpxy)
                        current_item['source'] = source_name
                        current_item['url'] = line
                        self.data[current_id] = current_item

    def filter(self):
        """Filter process."""
        internal_ids = list(self.data.keys())
        random.shuffle(internal_ids)
        pbar = tqdm(internal_ids, ascii=True)
        for internal_id in pbar:
            time.sleep(self.args.interval)
            url = self.data[internal_id]['url']
            status = 'OK'
            if self.args.min_height or self.args.resolution_on_title:
                height = utils.check_stream(url, self.args.timeout)
                if height == 0:
                    self.inaccessible_urls.add(url)
                    status = 'Inaccessible'
                elif height < self.args.min_height:
                    self.poor_urls.add(url)
                    status = 'Poor Resolution'
                self.data[internal_id]['height'] = height
            elif not utils.check_connectivity(url, self.args.timeout):
                self.inaccessible_urls.add(url)
                status = 'Inaccessible'
            pbar.write(f'{url}, {status}!')

    def __custom_sort(self, internal_id):
        """Sort by tvg-id, resolution and title."""
        res = []
        for key in self.args.sort_keys:
            entry = self.data[internal_id]
            if key == 'height':
                res.append(-entry.get(key, 0))
            elif key == 'title':
                res.append(entry.get(key, ''))
            elif key == 'tvg-id':
                res.append(int(entry['params'].get(key) or sys.maxsize))
        return res
