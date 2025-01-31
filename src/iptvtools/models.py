#!/usr/bin/env python
"""Playlist which contains all the channels' information.

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
from typing import Any

from tqdm import tqdm

from iptvtools import parsers, utils
from iptvtools.constants import defaults, tags


class Playlist:
    """Playlist model."""

    def __init__(
        self,
        channel_exclude: str,
        channel_include: str,
        group_exclude: str,
        group_include: str,
        max_height: int,
        min_height: int,
        inputs: list[str],
        interval: int,
        skip_connectivity_check: bool,
        output: str,
        replace_group_by_source: bool,
        resolution_on_title: bool,
        sort_keys: list[str],
        templates: list[str],
        timeout: int,
        udpxy: str,
    ) -> None:
        """Init for Playlist."""
        self.channel_exclude = channel_exclude
        self.channel_include = channel_include
        self.group_exclude = group_exclude
        self.group_include = group_include
        self.max_height = max_height
        self.min_height = min_height
        self.inputs = inputs
        self.interval = interval
        self.skip_connectivity_check = skip_connectivity_check
        self.output = output
        self.replace_group_by_source = replace_group_by_source
        self.resolution_on_title = resolution_on_title
        self.sort_keys = sort_keys
        self.templates = templates
        self.timeout = timeout
        self.udpxy = udpxy
        self.data: dict[str, Any] = {}
        self.id_url: dict[str, Any] = {}
        self.inaccessible_urls: set[str] = set()
        self.low_res_urls: set[str] = set()
        self.high_res_urls: set[str] = set()
        self.tvg_url = None

    def export(self) -> None:
        """Export playlist information."""
        res = []
        res.append(tags.M3U)
        if self.tvg_url is not None:
            res[0] += f' x-tvg-url="{self.tvg_url}"'
        for url in sorted(self.data, key=self.__custom_sort):
            if (
                url in self.inaccessible_urls
                or url in self.low_res_urls
                or url in self.high_res_urls
            ):
                continue

            entry = self.data[url]
            params_dict = entry.get("params", {})
            if self.replace_group_by_source:
                params_dict["group-title"] = self.data[url]["source"]
            params = " ".join(
                [f'{key}="{value}"' for key, value in params_dict.items()]
            )
            duration = entry["duration"]
            title = entry["title"]
            if self.resolution_on_title:
                height = self.data[url].get("height")
                title += f" [{utils.height_to_resolution(height)}]"

            res.append(f"{tags.INF}:{duration} {params},{title}\n{url}")

        with open(self.output, "w", encoding="utf-8") as f:
            f.write("\n".join(res))

    def parse(self) -> None:
        """Parse contents."""
        self._parse(self.inputs)
        logging.debug(self.data)
        self._parse(self.templates, is_template=True)
        logging.debug(self.data)

    def _parse(self, sources: list[str], is_template: bool = False) -> None:
        """Parse playlist sources."""
        template_order = 0
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
                        if res.get("tvg-url"):
                            self.tvg_url = res.get("tvg-url")
                        continue
                if skip:
                    skip = False
                    continue
                if line.startswith(tags.INF):
                    current_item = parsers.parse_tag_inf(line)
                    current_item = utils.unify_title_and_id(current_item)
                    current_id = current_item["id"]

                    params = current_item.get("params", {})
                    group = params.get("group-title", "")
                    if not skip and self.group_include:
                        if re.search(self.group_include, group):
                            logging.debug(f"Group to include: `{group}`.")
                        else:
                            skip = True
                    if (
                        not skip
                        and self.group_exclude
                        and re.search(self.group_exclude, group)
                    ):
                        skip = True
                        logging.debug(f"Group to exclude: `{group}`.")

                    title = current_item.get("title", "")
                    if not skip and self.channel_include:
                        if re.search(self.channel_include, title):
                            logging.debug(f"Channel to include: `{title}`.")
                        else:
                            skip = True
                    if (
                        not skip
                        and self.channel_exclude
                        and re.search(self.channel_exclude, title)
                    ):
                        skip = True
                        logging.debug(f"Channel to exclude: `{title}`.")

                else:
                    if is_template:
                        template_order = template_order + 1
                        for url in self.id_url.get(current_id, []):
                            current_params = current_item["params"]
                            current_params["template-order"] = template_order
                            self.data[url]["params"].update(current_params)
                            self.data[url]["title"] = current_item["title"]
                    else:
                        if self.udpxy:
                            line = utils.convert_url_with_udpxy(line, self.udpxy)
                        current_item["source"] = source_name
                        self.data[line] = current_item

                        if current_id not in self.id_url:
                            self.id_url[current_id] = []
                        self.id_url[current_id].append(line)

    def filter(self) -> None:
        """Filter process."""
        urls = list(self.data.keys())
        random.shuffle(urls)
        pbar = tqdm(urls, ascii=True)
        for url in pbar:
            status = "OK"
            time.sleep(self.interval)
            if self.skip_connectivity_check:
                status = "Skipped"
            elif self.max_height or self.min_height or self.resolution_on_title:
                height = utils.check_stream(url, self.timeout)
                if height == 0:
                    self.inaccessible_urls.add(url)
                    status = "Inaccessible (0 height)"
                elif height < self.min_height:
                    self.low_res_urls.add(url)
                    status = "Low Resolution"
                elif (
                    self.max_height != defaults.MAX_HEIGHT and height > self.max_height
                ):
                    self.high_res_urls.add(url)
                    status = "High Resolution"
                self.data[url]["height"] = height
            elif not utils.check_connectivity(url, self.timeout):
                self.inaccessible_urls.add(url)
                status = "Inaccessible (No connectivity)"
            pbar.write(f"{url}, {status}!")

    def __custom_sort(self, url: str) -> list[Any]:
        """Sort by tvg-id, resolution, template-order and title."""
        res = []
        for key in self.sort_keys:
            entry = self.data[url]
            if key == "height":
                res.append(-entry.get(key, 0))
            elif key == "title":
                res.append(entry.get(key, ""))
            elif key == "tvg-id":
                res.append(
                    int(re.sub(r"\D", "", entry["params"].get(key, "")) or sys.maxsize)
                )
            elif key == "template-order":
                res.append(int(entry["params"].get(key) or sys.maxsize))
            elif key == "group-title":
                res.append(entry["params"].get(key) or "")
        return res
