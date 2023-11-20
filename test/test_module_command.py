import os

import pytest
from pathlib import Path
from click.testing import CliRunner
import cbot.defaults
from cbot.cbot import cbot


def test_module_create_in_empty_directory_fails(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['module', 'create'])
        assert result.exit_code != 0


def test_module_create_in_newly_created_project_succeeds(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['new', 'blerg'])
        assert result.exit_code == 0
        os.chdir('blerg')
        result = runner.invoke(cbot.cbot.cli, ['module', 'create', 'my_module'])
        assert result.exit_code == 0


def test_module_create_in_newly_created_project_creates_files(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['new', 'blerg'])
        assert result.exit_code == 0
        os.chdir('blerg')
        result = runner.invoke(cbot.cbot.cli, ['module', 'create', 'my_module'])
        assert Path(cbot.defaults.DEFAULT_SOURCE_DIR, 'my_module.c').exists()
        assert Path(cbot.defaults.DEFAULT_INCLUDE_DIR, 'my_module.h').exists()
        assert Path(cbot.defaults.DEFAULT_TEST_DIR, 'test_my_module.c').exists()
        assert '#define MY_MODULE_H' in Path(cbot.defaults.DEFAULT_INCLUDE_DIR, 'my_module.h').read_text()
        assert '#include "my_module.h"' in Path(cbot.defaults.DEFAULT_SOURCE_DIR, 'my_module.c').read_text()
        assert 'void test_my_module_NeedToImplement(void)' in Path(cbot.defaults.DEFAULT_TEST_DIR, 'test_my_module.c').read_text()


def test_module_create_in_submodule(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(tmp_path):
        result = runner.invoke(cbot.cbot.cli, ['new', 'blerg'])
        assert result.exit_code == 0
        os.chdir('blerg')
        result = runner.invoke(cbot.cbot.cli, ['module', 'create', 'my_submodule/my_module'])
        assert Path(cbot.defaults.DEFAULT_SOURCE_DIR, 'my_submodule', 'my_module.c').exists()
        assert Path(cbot.defaults.DEFAULT_INCLUDE_DIR, 'my_submodule', 'my_module.h').exists()
        assert Path(cbot.defaults.DEFAULT_TEST_DIR, 'my_submodule', 'test_my_module.c').exists()
        assert '#define MY_MODULE_H' in Path(cbot.defaults.DEFAULT_INCLUDE_DIR, 'my_submodule', 'my_module.h').read_text()
        assert '#include "my_module.h"' in Path(cbot.defaults.DEFAULT_SOURCE_DIR, 'my_submodule', 'my_module.c').read_text()
        assert 'void test_my_module_NeedToImplement(void)' in Path(cbot.defaults.DEFAULT_TEST_DIR, 'my_submodule', 'test_my_module.c').read_text()

