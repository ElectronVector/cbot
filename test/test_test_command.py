import os

import pytest
from pathlib import Path
from click.testing import CliRunner
import cbot.defaults
from cbot.cbot import cbot


def test_test_runner_creates_runner_files(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['test', 'generate-runners'])
        assert result.exit_code == 0
