# For building applications and tests with CMake.
import shutil
import subprocess
import sys
from pathlib import Path

import click

DEFAULT_BUILD_DIR = 'build'


@click.command()
def run():
    """ Run the project binary in the current folder.
    """
    binary_path = Path(DEFAULT_BUILD_DIR) / Path.cwd().stem
    click.echo(f"Running '{binary_path}'...")
    return subprocess.run([binary_path]).returncode