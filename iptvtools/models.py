#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Playlist which contains all the channels' information.

File: models.py
Author: huxuan
Email: i(at)huxuan.org
"""
import logging
import os.path
import random
import re
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
        self.id_url = {}
        self.inaccessible_urls = set()
        self.poor_urls = set()
        self.tvg_url = None

    def export(self):
        """Export playlist information."""
        res = []
        res.append(tags.M3U)
        if self.tvg_url is not None:
            res[0] += f' x-tvg-url="{self.tvg_url}"'
        for url in sorted(self.data, key=self.__custom_sort):

            if url in self.inaccessible_urls or url in self.poor_urls:
                continue

            entry = self.data[url]
            params_dict = entry.get('params', {})
            if self.args.replace_group_by_source:
                params_dict['group-title'] = self.data[url]['source']
            params = ' '.join([
                f'{key}="{value}"'
                for key, value in params_dict.items()
            ])
            duration = entry['duration']
            title = entry['title']
            if self.args.resolution_on_title:
                height = self.data[url].get('height')
                title += f' [{utils.height_to_resolution(height)}]'

            res.append(
                f'{tags.INF}:{duration} {params},{title}\n{url}')

        open(self.args.output, 'w', encoding='utf-8').write('\n'.join(res))

    def parse(self):
        """Parse contents."""
        self._parse(self.args.inputs)
        logging.debug(self.data)
        self._parse(self.args.templates, is_template=True)
        logging.debug(self.data)

    def _parse(self, sources, is_template=False):
        """Parse playlist sources."""
        for source in sources:
            source_name = os.path.splitext(os.path.basename(source))[0]
            current_item = {}
            skip = False
            is_first_line = True
            for line in parsers.parse_content_to_lines(source):
                if not line:
                    continue
                if is_first_line:
                    is_first_line = False
                    if line.startswith(tags.M3U):
                        res = parsers.parse_tag_m3u(line)
                        if res.get('tvg-url'):
                            self.tvg_url = res.get('tvg-url')
                        continue
                if skip:
                    skip = False
                    continue
                if line.startswith(tags.INF):
                    current_item = parsers.parse_tag_inf(line)
                    current_item = utils.unify_title_and_id(current_item)
                    current_id = current_item['id']

                    params = current_item.get('params', {})
                    group = params.get('group-title', '')
                    if not skip and self.args.group_include:
                        if re.search(self.args.group_include, group):
                            logging.debug(f'Group to include: `{group}`.')
                        else:
                            skip = True
                    if not skip and self.args.group_exclude and \
                            re.search(self.args.group_exclude, group):
                        skip = True
                        logging.debug(f'Group to exclude: `{group}`.')

                    title = current_item.get('title', '')
                    if not skip and self.args.channel_include:
                        if re.search(self.args.channel_include, title):
                            logging.debug(f'Channel to include: `{title}`.')
                        else:
                            skip = True
                    if not skip and self.args.channel_exclude and \
                            re.search(self.args.channel_exclude, title):
                        skip = True
                        logging.debug(f'Channel to exclude: `{title}`.')

                else:
                    if is_template:
                        for url in self.id_url.get(current_id, []):
                            current_params = current_item['params']
                            self.data[url]['params'].update(current_params)
                            self.data[url]['title'] = current_item['title']
                    else:
                        if self.args.udpxy:
                            line = utils.convert_url_with_udpxy(
                                line, self.args.udpxy)
                        current_item['source'] = source_name
                        self.data[line] = current_item

                        if current_id not in self.id_url:
                            self.id_url[current_id] = []
                        self.id_url[current_id].append(line)

    def filter(self):
        """Filter process."""
        urls = list(self.data.keys())
        random.shuffle(urls)
        pbar = tqdm(urls, ascii=True)
        for url in pbar:
            time.sleep(self.args.interval)
            status = 'OK'
            if self.args.min_height or self.args.resolution_on_title:
                height = utils.check_stream(url, self.args.timeout)
                if height == 0:
                    self.inaccessible_urls.add(url)
                    status = 'Inaccessible'
                elif height < self.args.min_height:
                    self.poor_urls.add(url)
                    status = 'Poor Resolution'
                self.data[url]['height'] = height
            elif not utils.check_connectivity(url, self.args.timeout):
                self.inaccessible_urls.add(url)
                status = 'Inaccessible'
            pbar.write(f'{url}, {status}!')

    def __custom_sort(self, url):
        """Sort by tvg-id, resolution and title."""
        res = []
        for key in self.args.sort_keys:
            entry = self.data[url]
            if key == 'height':
                res.append(-entry.get(key, 0))
            elif key == 'title':
                res.append(entry.get(key, ''))
            elif key == 'tvg-id':
                res.append(int(entry['params'].get(key) or sys.maxsize))
            elif key == 'group-title':
                res.append(entry['params'].get(key) or '')
        return res
