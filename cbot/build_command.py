# For building applications and tests with CMake.
import shutil
import subprocess
from pathlib import Path


def execute():
    print(Path.cwd())
    if Path('build').exists():
        shutil.rmtree('build')
    result = subprocess.run(['cmake', '-S', '.', '-B', 'build']).returncode
    return subprocess.run(['cmake', '--build', 'build']).returncode