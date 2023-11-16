# Test the new module for new project creation.
import shutil
from pathlib import Path
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


def test_new_doesnt_create_folder_if_target_path_doesnt_exist():
    new_project_name = 'example'
    with pytest.raises(TargetDirNotFoundError):
        new(TEST_DATA_DIR, new_project_name)


def test_new_creates_src_folder():
    pass


def test_new_creates_inc_folder():
    pass


def test_new_creates_test_folder():
    pass


def test_new_creates_cmakelists():
    pass


def test_new_creates_main():
    pass


def test_new_creates_a_buildable_project():
    pass
