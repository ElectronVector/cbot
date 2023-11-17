import sys
from pathlib import Path

import click

import cbot.new
import cbot.build_command


@click.group()
def cli():
    pass


@click.command()
@click.argument('project_name')
def new(project_name):
    """ Create a new cbot project in the current directory.

    PROJECT_NAME is the name of the new project to create. A directory with this name must not already exist.
    """
    if Path.exists(Path(project_name)):
        click.echo(f"Error: a directory named '{project_name}' already exists")
        return -1

    click.echo(f"Creating new project '{project_name}'...")
    cbot.new.new('.', project_name)


cli.add_command(new)


@click.command()
def build():
    """ Build the project in the current folder with CMake.

    Reload all CMake files and execute the build.
    """
    if not Path('CMakeLists.txt').exists():
        click.echo(f"Error: a 'CMakeLists.txt' file was not found")
        sys.exit(-1)

    click.echo(f"Building...")
    sys.exit(cbot.build_command.execute())


cli.add_command(build)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli()
