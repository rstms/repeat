# cli tests

import pytest

from repeat import cli


def test_cli(cli_runner):
    result = cli_runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert 'Usage:' in result.output
