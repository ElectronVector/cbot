from pathlib import Path

import click


@click.group()
def cli():
    pass


@click.command()
@click.argument('project_name')
def new(project_name):
    """ Create a new cbot project in a new subdirectory in the current directory.

    PROJECT_NAME is the name of the new project to create. A directory with this name must not already exist.
    """
    if Path.exists(Path(project_name)):
        click.echo(f"Error: a directory named '{project_name}' already exists")
        exit(-1)

    click.echo(f"Creating new project '{project_name}'...")


cli.add_command(new)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli()
