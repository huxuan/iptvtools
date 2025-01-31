"""Test for cli."""

from click.testing import CliRunner

from iptvtools.cli import cli


def test_cli() -> None:
    """Test for cli."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Usage" in result.output


def test_cli_filter_help() -> None:
    """Test the help for filter subcommand of the cli."""
    runner = CliRunner()
    result = runner.invoke(cli, ["filter", "--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output
