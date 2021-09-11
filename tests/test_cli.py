# cli tests

import pytest
import subprocess

from repeat import cli


def run(cmd):
    return subprocess.run(cmd, check=True, text=True, capture_output=True, shell=True)


def test_cli_usage(cli_runner):
    result = cli_runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert 'Usage:' in result.output


def test_shell_none():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat")
    assert buffer.stdout == '1\n2\n3\n'


def test_shell_count_zero():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat 0")
    assert buffer.stdout == ''


def test_shell_count_zero_length():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat 0 -l")
    assert buffer.stdout == '3\n'


def test_shell_length_count_zero():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat -l 0")
    assert buffer.stdout == '3\n'


def test_shell_count_one():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat 1")
    assert buffer.stdout == '1\n2\n3\n'


def test_shell_count_two():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat 2")
    assert buffer.stdout == '1\n2\n3\n1\n2\n3\n'


def test_shell_length_only():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat -l")
    assert buffer.stdout == '3\n1\n2\n3\n'


def test_shell_both():
    buffer = run("/bin/echo -e '1\n2\n3' | repeat 2 -l")
    assert buffer.stdout == '3\n1\n2\n3\n1\n2\n3\n'
