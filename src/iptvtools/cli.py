"""Command Line Interface."""

import click


@click.group()
def cli() -> None:
    """CLI for IPTVTools."""


@cli.command()
def run() -> None:
    """Run command."""
