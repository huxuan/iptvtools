"""Command Line Interface."""

import click


@click.group()
@click.version_option()
def cli() -> None:
    """CLI for IPTVTools."""


@cli.command()
def run() -> None:
    """Run command."""
