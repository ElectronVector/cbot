import subprocess
from pathlib import Path
import click
import cbot.defaults


@click.command()
def run():
    """ Run the project binary in the current folder.
    """
    binary_path = Path(cbot.defaults.DEFAULT_BUILD_DIR) / Path.cwd().stem
    click.echo(f"Running '{binary_path}'...")
    return subprocess.run([binary_path]).returncode
