import sys
from pathlib import Path

import click
import jinja2

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
    template_location = Path(__file__).parent / 'templates' / 'module'
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=template_location))

    template = environment.get_template('header.h')
    with Path(cwd, cbot.defaults.DEFAULT_INCLUDE_DIR, f'{module_name}.h').open(mode='w') as f:
        f.write(template.render(module_name=module_name))

    template = environment.get_template('source.c')
    with Path(cwd, cbot.defaults.DEFAULT_SOURCE_DIR, f'{module_name}.c').open(mode='w') as f:
        f.write(template.render(module_name=module_name))

    template = environment.get_template('test.c')
    with Path(cwd, cbot.defaults.DEFAULT_TEST_DIR, f'test_{module_name}.c').open(mode='w') as f:
        f.write(template.render(module_name=module_name))


module.add_command(create)
