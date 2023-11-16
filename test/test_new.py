# Test the new module for new project creation.
import shutil
from pathlib import Path

import jinja2 as jinja2
import pytest

from cbot.new import new, TargetDirNotFoundError

TEST_DATA_DIR = '.test_data'


@pytest.fixture()
def test_data_dir():
    # Create a clean test data directory.
    if Path.exists(Path(TEST_DATA_DIR)):
        # Check if it was left over from a previous run.
        shutil.rmtree(TEST_DATA_DIR)
    Path.mkdir(Path(TEST_DATA_DIR))
    yield
    # Remove the test data directory.
    if Path.exists(Path(TEST_DATA_DIR)):
        shutil.rmtree(TEST_DATA_DIR)


def test_new_creates_folder_if_it_doesnt_exist(test_data_dir):
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name))


def test_new_doesnt_create_folder_if_it_exists(test_data_dir):
    new_project_name = 'example'
    Path.mkdir(Path(TEST_DATA_DIR, new_project_name))
    new(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name))


def test_new_doesnt_create_folder_if_target_path_doesnt_exist(test_data_dir):
    new_project_name = 'example'
    with pytest.raises(TargetDirNotFoundError):
        new('dir_that_doesnt_exist', new_project_name)


def test_new_creates_src_folder(test_data_dir):
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, 'src'))


def test_new_creates_inc_folder(test_data_dir):
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, 'src'))


def test_new_creates_test_folder(test_data_dir):
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, 'test'))


def test_new_creates_cmakelists(test_data_dir):
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, 'CMakeLists.txt'))


def test_new_creates_main(test_data_dir):
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, 'src', 'main.c'))


def test_new_contains_message_with_project_name(test_data_dir):
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    with Path(TEST_DATA_DIR, 'example', 'src', 'main.c').open() as f:
        file_contents = f.read()
    assert 'Running example from main()...' in file_contents


def test_new_contains_message_with_a_different_project_name(test_data_dir):
    new_project_name = 'example2'
    new(TEST_DATA_DIR, new_project_name)
    with Path(TEST_DATA_DIR, 'example2', 'src', 'main.c').open() as f:
        file_contents = f.read()
    assert 'Running example2 from main()...' in file_contents


def test_new_creates_a_buildable_project():
    pass
