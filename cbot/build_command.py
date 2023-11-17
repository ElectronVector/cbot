# For building applications and tests with CMake.
import shutil
import subprocess
from pathlib import Path


def run():
    print(Path.cwd())
    if Path('build').exists():
        shutil.rmtree('build')
    return subprocess.run(['cmake', '-S', '.', '-B', 'build']).returncode