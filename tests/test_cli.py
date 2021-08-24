# cli tests

import pytest

from repeat import cli
from subprocess import check_output


def test_cli(cli_runner):
    result = cli_runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert 'Usage:' in result.output


def test_shell_none():
    buffer = check_output("echo -e '1\n2\n3' | repeat", shell=True)
    output = buffer.decode()
    assert output == '1\n2\n3\n'


def test_shell_count_zero():
    buffer = check_output("echo -e '1\n2\n3' | repeat 0", shell=True)
    output = buffer.decode()
    assert output == ''


def test_shell_count_zero_length():
    buffer = check_output("echo -e '1\n2\n3' | repeat 0 -l", shell=True)
    output = buffer.decode()
    assert output == '3\n'


def test_shell_length_count_zero():
    buffer = check_output("echo -e '1\n2\n3' | repeat -l 0", shell=True)
    output = buffer.decode()
    assert output == '3\n'


def test_shell_count_one():
    buffer = check_output("echo -e '1\n2\n3' | repeat 1", shell=True)
    output = buffer.decode()
    assert output == '1\n2\n3\n'


def test_shell_count_two():
    buffer = check_output("echo -e '1\n2\n3' | repeat 2", shell=True)
    output = buffer.decode()
    assert output == '1\n2\n3\n1\n2\n3\n'


def test_shell_length_only():
    buffer = check_output("echo -e '1\n2\n3' | repeat -l", shell=True)
    output = buffer.decode()
    assert output == '3\n1\n2\n3\n'


def test_shell_both():
    buffer = check_output("echo -e '1\n2\n3' | repeat 2 -l", shell=True)
    output = buffer.decode()
    assert output == '3\n1\n2\n3\n1\n2\n3\n'
