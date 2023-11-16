from pathlib import Path

import jinja2

TEMPLATE_PATH = 'cbot/templates/'

DEFAULT_TEST_DIR = 'test'
DEFAULT_INCLUDE_DIR = 'src'
DEFAULT_SOURCE_DIR = 'src'


class TargetDirNotFoundError(Exception):
    """Raise when the target directory for the new project cannot be found."""


def new(target_dir, project_name):
    # Check that the target directory exists.
    if not Path.exists(Path(target_dir)):
        raise TargetDirNotFoundError(f"Target directory '{target_dir}' not found")

    # Create the new project directory if necessary.
    new_project_dir = Path(target_dir, project_name)
    if not Path.exists(new_project_dir):
        Path.mkdir(new_project_dir)

    # Create the internal project directories.

    create_default_internal_dir_if_necessary(new_project_dir, DEFAULT_SOURCE_DIR)
    create_default_internal_dir_if_necessary(new_project_dir, DEFAULT_INCLUDE_DIR)
    create_default_internal_dir_if_necessary(new_project_dir, DEFAULT_TEST_DIR)

    generate_file_from_template(new_project_dir, project_name, 'CMakeLists.txt')
    generate_file_from_template(new_project_dir, project_name, 'src/main.c')


def generate_file_from_template(project_path, project_name, project_file_path):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=TEMPLATE_PATH))
    template = environment.get_template(project_file_path)
    with Path(project_path, project_file_path).open(mode='w') as f:
        f.write(template.render(project_name=project_name))


def create_default_internal_dir_if_necessary(new_project_dir, internal_dir):
    new_dir = Path(new_project_dir, internal_dir)
    if not Path.exists(new_dir):
        Path.mkdir(new_dir)
