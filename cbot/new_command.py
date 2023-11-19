from pathlib import Path

import click
import jinja2

import cbot.defaults


class TargetDirNotFoundError(Exception):
    """Raise when the target directory for the new project cannot be found."""


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
    execute('.', project_name)


def execute(target_dir, project_name):
    # Check that the target directory exists.
    if not Path.exists(Path(target_dir)):
        raise TargetDirNotFoundError(f"Target directory '{target_dir}' not found")

    # Create the new project directory if necessary.
    new_project_dir = Path(target_dir, project_name)
    if not Path.exists(new_project_dir):
        Path.mkdir(new_project_dir)

    # Create the internal project directories.
    create_default_internal_dir_if_necessary(new_project_dir, cbot.defaults.DEFAULT_SOURCE_DIR)
    create_default_internal_dir_if_necessary(new_project_dir, cbot.defaults.DEFAULT_INCLUDE_DIR)
    create_default_internal_dir_if_necessary(new_project_dir, cbot.defaults.DEFAULT_TEST_DIR)

    generate_file_from_template(new_project_dir, project_name, 'CMakeLists.txt')
    generate_file_from_template(new_project_dir, project_name, f'{cbot.defaults.DEFAULT_SOURCE_DIR}/main.c')


def generate_file_from_template(project_path, project_name, project_file_path):
    template_location = Path(__file__).parent / 'templates' / 'project'
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=template_location))
    template = environment.get_template(project_file_path)
    with Path(project_path, project_file_path).open(mode='w') as f:
        f.write(template.render(project_name=project_name))


def create_default_internal_dir_if_necessary(new_project_dir, internal_dir):
    new_dir = Path(new_project_dir, internal_dir)
    if not Path.exists(new_dir):
        Path.mkdir(new_dir)

