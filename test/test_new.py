# Test the new module for new project creation.
import pytest
import shutil
from pathlib import Path

from cbot.new_command import execute, TargetDirNotFoundError
import cbot.defaults

TEST_DATA_DIR = '.test_data'


# Todo: Use tmp_dir provided by pytest, and the isolated_filesystem provided by click.
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
    execute(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name))


def test_new_doesnt_create_folder_if_it_exists(test_data_dir):
    new_project_name = 'example'
    Path.mkdir(Path(TEST_DATA_DIR, new_project_name))
    execute(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name))


def test_new_doesnt_create_folder_if_target_path_doesnt_exist(test_data_dir):
    new_project_name = 'example'
    with pytest.raises(TargetDirNotFoundError):
        execute('dir_that_doesnt_exist', new_project_name)


def test_new_creates_src_folder(test_data_dir):
    new_project_name = 'example'
    execute(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, cbot.defaults.DEFAULT_SOURCE_DIR))


def test_new_creates_inc_folder(test_data_dir):
    new_project_name = 'example'
    execute(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, cbot.defaults.DEFAULT_SOURCE_DIR))


def test_new_creates_test_folder(test_data_dir):
    new_project_name = 'example'
    execute(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, cbot.defaults.DEFAULT_TEST_DIR))


def test_new_creates_cmakelists(test_data_dir):
    new_project_name = 'example'
    execute(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, 'CMakeLists.txt'))


def test_new_creates_main(test_data_dir):
    new_project_name = 'example'
    execute(TEST_DATA_DIR, new_project_name)
    assert Path.exists(Path(TEST_DATA_DIR, new_project_name, cbot.defaults.DEFAULT_SOURCE_DIR, 'main.c'))


def test_new_main_contains_message_with_project_name(test_data_dir):
    new_project_name = 'example'
    execute(TEST_DATA_DIR, new_project_name)
    assert 'Running example from main()...' in Path(TEST_DATA_DIR, 'example', cbot.defaults.DEFAULT_SOURCE_DIR, 'main.c').read_text()


def test_new_cmakelists_contains_project_name(test_data_dir):
    new_project_name = 'example'
    execute(TEST_DATA_DIR, new_project_name)
    assert 'project(example C)' in Path(TEST_DATA_DIR, 'example', 'CMakeLists.txt').read_text()
