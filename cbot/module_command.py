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

    module_path = Path(module_name).parents[0]
    module_name = Path(module_name).stem

    click.echo(f'****{module_path}****')
    click.echo(f'****{module_name}****')

    if not (cbot.defaults.DEFAULT_INCLUDE_DIR / module_path).exists():
        (cbot.defaults.DEFAULT_INCLUDE_DIR / module_path).mkdir(parents=True, exist_ok=True)

    # Generate the include guard string.
    include_guard_str = list(module_path.parts)
    include_guard_str += [module_name]
    include_guard_str = '_'.join(include_guard_str).upper() + '_H'
    click.echo(f'****{include_guard_str}****')

    template = environment.get_template('header.h')
    with Path(cwd, cbot.defaults.DEFAULT_INCLUDE_DIR, module_path, f'{module_name}.h').open(mode='w') as f:
        f.write(template.render(include_guard_str=include_guard_str))

    if not (cbot.defaults.DEFAULT_SOURCE_DIR / module_path).exists():
        (cbot.defaults.DEFAULT_SOURCE_DIR / module_path).mkdir(parents=True, exist_ok=True)

    template = environment.get_template('source.c')
    with Path(cwd, cbot.defaults.DEFAULT_SOURCE_DIR, module_path, f'{module_name}.c').open(mode='w') as f:
        f.write(template.render(module_name=module_name))

    if not (cbot.defaults.DEFAULT_TEST_DIR / module_path).exists():
        (cbot.defaults.DEFAULT_TEST_DIR / module_path).mkdir(parents=True, exist_ok=True)

    template = environment.get_template('test.c')
    with Path(cwd, cbot.defaults.DEFAULT_TEST_DIR, module_path, f'test_{module_name}.c').open(mode='w') as f:
        f.write(template.render(module_name=module_name))


module.add_command(create)
