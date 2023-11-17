# For building applications and tests with CMake.
import shutil
import subprocess
import sys
from pathlib import Path

import click

DEFAULT_BUILD_DIR = 'build'


@click.command()
def build():
    """ Build the project in the current folder with CMake.

    Reload all CMake files and execute the build.
    """
    if not Path('CMakeLists.txt').exists():
        click.echo(f"Error: a 'CMakeLists.txt' file was not found")
        sys.exit(-1)

    click.echo(f"Building...")
    sys.exit(execute())


def execute():
    print(Path.cwd())

    if Path(DEFAULT_BUILD_DIR).exists():
        shutil.rmtree(DEFAULT_BUILD_DIR)

    result = subprocess.run(['cmake', '-S', '.', '-B', DEFAULT_BUILD_DIR]).returncode

    if result == 0:
        result = subprocess.run(['cmake', '--build', DEFAULT_BUILD_DIR]).returncode
    return result
