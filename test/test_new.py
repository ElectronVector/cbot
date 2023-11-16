# Test the new module for new project creation.
import os
import shutil
from pathlib import Path

from cbot.new import new

TEST_DATA_DIR = '.test_data'


def test_new_creates_folder_if_it_doesnt_exist():
    if Path.exists(Path(TEST_DATA_DIR)):
        shutil.rmtree(TEST_DATA_DIR)
    Path.mkdir(Path(TEST_DATA_DIR))
    new_project_name = 'example'
    new(TEST_DATA_DIR, new_project_name)
    assert(Path.exists(Path(TEST_DATA_DIR, new_project_name)))


def test_new_doesnt_create_folder_if_it_exists():
    pass


def test_new_doesnt_create_folder_if_target_path_doesnt_exist():
    pass


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