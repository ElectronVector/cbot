import pytest
from pathlib import Path
from click.testing import CliRunner
from cbot.cbot import cbot


def test_help_function(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['--help'])
    assert result.exit_code == 0


def test_new_creates_new_project(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['new', 'blerg'])
        assert Path('blerg').exists()
        assert Path('blerg/CMakeLists.txt').exists()
        assert Path('blerg/src').exists()
        assert Path('blerg/test').exists()
        assert Path('blerg/src/main.c').exists()
        assert result.exit_code == 0

