import sys
from pathlib import Path

import click

import cbot.defaults


@click.group()
def module():
    """ Create a new module consisting of a .c, .h and test file.
    """
    if not Path('CMakeLists.txt').exists():
        raise FileNotFoundError('CMakeLists.txt')
    # Todo: Check for src, include and test folders.


@click.command()
@click.argument('module_name')
def create(module_name):
    click.echo(f"Creating module '{module_name}'...")
    cwd = Path.cwd()

    Path(cwd, cbot.defaults.DEFAULT_SOURCE_DIR, f'{module_name}.c').touch()
    Path(cwd, cbot.defaults.DEFAULT_INCLUDE_DIR, f'{module_name}.h').touch()
    Path(cwd, cbot.defaults.DEFAULT_TEST_DIR, f'test_{module_name}.c').touch()


module.add_command(create)
