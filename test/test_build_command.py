import os

import pytest
from pathlib import Path
from click.testing import CliRunner
from cbot.cbot import cbot


def test_build_in_empty_directory_fails(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['build'])
        assert result.exit_code != 0


def test_build_in_new_created_project_succeeds(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['new', 'blerg'])
        assert result.exit_code == 0
        os.chdir('blerg')
        result = runner.invoke(cbot.cbot.cli, ['build'])
        assert result.exit_code == 0


def test_build_in_new_created_project_creates_a_binary(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['new', 'blerg'])
        assert result.exit_code == 0
        os.chdir('blerg')
        result = runner.invoke(cbot.cbot.cli, ['build'])
        assert Path('build/blerg').exists()

