"""Command Line Interface."""

import logging
import shutil

import click

from iptvtools import exceptions
from iptvtools.config import Config
from iptvtools.constants import defaults, helps
from iptvtools.models import Playlist


@click.group(
    context_settings={"show_default": True},
)
@click.version_option()
def cli() -> None:
    """CLI for IPTVTools."""


@cli.command()
@click.option("--channel-exclude", help=helps.CHANNEL_EXCLUDE)
@click.option("--channel-include", help=helps.CHANNEL_INCLUDE)
@click.option("--group-exclude", help=helps.GROUP_EXCLUDE)
@click.option("--group-include", help=helps.GROUP_INCLUDE)
@click.option(
    "--max-height", default=defaults.MAX_HEIGHT, type=int, help=helps.MAX_HEIGHT
)
@click.option(
    "--min-height", default=defaults.MIN_HEIGHT, type=int, help=helps.MIN_HEIGHT
)
@click.option("-c", "--config", default=defaults.CONFIG, help=helps.CONFIG)
@click.option(
    "-i", "--inputs", multiple=True, default=defaults.INPUTS, help=helps.INPUTS
)
@click.option(
    "-I", "--interval", default=defaults.INTERVAL, type=int, help=helps.INTERVAL
)
@click.option("-L", "--log-level", default=defaults.LOG_LEVEL, help=helps.LOG_LEVEL)
@click.option(
    "-n",
    "--skip-connectivity-check",
    is_flag=True,
    help=helps.SKIP_CONNECTIVITY_CHECK,
)
@click.option("-o", "--output", default=defaults.OUTPUT, help=helps.OUTPUT)
@click.option(
    "-r",
    "--replace-group-by-source",
    is_flag=True,
    help=helps.REPLACE_GROUP_BY_SOURCE,
)
@click.option(
    "-R",
    "--resolution-on-title",
    is_flag=True,
    help=helps.RESOLUTION_ON_TITLE,
)
@click.option(
    "-s", "--sort-keys", multiple=True, default=defaults.SORT_KEYS, help=helps.SORT_KEYS
)
@click.option(
    "-t", "--templates", multiple=True, default=defaults.TEMPLATES, help=helps.TEMPLATES
)
@click.option("-T", "--timeout", default=defaults.TIMEOUT, type=int, help=helps.TIMEOUT)
@click.option("-u", "--udpxy", default=defaults.UDPXY, help=helps.UDPXY)
def filter(
    channel_exclude: str,
    channel_include: str,
    group_exclude: str,
    group_include: str,
    max_height: int,
    min_height: int,
    config: str,
    inputs: list[str],
    interval: int,
    log_level: str,
    skip_connectivity_check: bool,
    output: str,
    replace_group_by_source: bool,
    resolution_on_title: bool,
    sort_keys: list[str],
    templates: list[str],
    timeout: int,
    udpxy: str,
) -> None:
    """Filter m3u playlists."""
    logging.basicConfig(level=log_level.upper())

    if (max_height or min_height or resolution_on_title) and shutil.which(
        "ffprobe"
    ) is None:
        raise exceptions.FFmpegNotInstalledError()

    Config.init(config)
    playlist = Playlist(
        channel_exclude,
        channel_include,
        group_exclude,
        group_include,
        max_height,
        min_height,
        inputs,
        interval,
        skip_connectivity_check,
        output,
        replace_group_by_source,
        resolution_on_title,
        sort_keys,
        templates,
        timeout,
        udpxy,
    )
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
