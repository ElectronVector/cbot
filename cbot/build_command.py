# For building applications and tests with CMake.
import shutil
import subprocess
from pathlib import Path

DEFAULT_BUILD_DIR = 'build'


def execute():
    print(Path.cwd())

    if Path(DEFAULT_BUILD_DIR).exists():
        shutil.rmtree(DEFAULT_BUILD_DIR)

    result = subprocess.run(['cmake', '-S', '.', '-B', DEFAULT_BUILD_DIR]).returncode

    if result == 0:
        result = subprocess.run(['cmake', '--build', DEFAULT_BUILD_DIR]).returncode
    return result
