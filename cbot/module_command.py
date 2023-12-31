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

    if not (cbot.defaults.DEFAULT_INCLUDE_DIR / module_path).exists():
        (cbot.defaults.DEFAULT_INCLUDE_DIR / module_path).mkdir(parents=True, exist_ok=True)

    # Generate the include guard string.
    include_guard_str = '_'.join(list(module_path.parts) + [module_name]).upper() + '_H'

    template = environment.get_template('header.h')
    with Path(cwd, cbot.defaults.DEFAULT_INCLUDE_DIR, module_path, f'{module_name}.h').open(mode='w') as f:
        f.write(template.render(include_guard_str=include_guard_str))

    if not (cbot.defaults.DEFAULT_SOURCE_DIR / module_path).exists():
        (cbot.defaults.DEFAULT_SOURCE_DIR / module_path).mkdir(parents=True, exist_ok=True)

    # Generate the string used to include the header file. Use forward slashes no matter the platform we are on.
    include_str = '/'.join(list(module_path.parts) + [module_name]) + '.h'

    template = environment.get_template('source.c')
    with Path(cwd, cbot.defaults.DEFAULT_SOURCE_DIR, module_path, f'{module_name}.c').open(mode='w') as f:
        f.write(template.render(include_str=include_str))

    if not (cbot.defaults.DEFAULT_TEST_DIR / module_path).exists():
        (cbot.defaults.DEFAULT_TEST_DIR / module_path).mkdir(parents=True, exist_ok=True)

    template = environment.get_template('test.c')
    with Path(cwd, cbot.defaults.DEFAULT_TEST_DIR, module_path, f'test_{module_name}.c').open(mode='w') as f:
        f.write(template.render(module_name=module_name, include_str=include_str))


@click.command()
@click.argument('module_name')
def destroy(module_name):
    click.echo(f"Destroying module '{module_name}'...")

    cwd = Path.cwd()
    module_path = Path(module_name).parents[0]
    module_name = Path(module_name).stem

    Path(cwd, cbot.defaults.DEFAULT_SOURCE_DIR, module_path, f'{module_name}.c').unlink()
    Path(cwd, cbot.defaults.DEFAULT_INCLUDE_DIR, module_path, f'{module_name}.h').unlink()
    Path(cwd, cbot.defaults.DEFAULT_TEST_DIR, module_path, f'test_{module_name}.c').unlink()


module.add_command(create)
module.add_command(destroy)
