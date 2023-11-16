from pathlib import Path


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
    source_dir = Path(new_project_dir, 'src')
    include_dir = Path(new_project_dir, 'src')
    test_dir = Path(new_project_dir, 'test')
    if not Path.exists(source_dir):
        Path.mkdir(source_dir)
    if not Path.exists(include_dir):
        Path.mkdir(include_dir)
    if not Path.exists(test_dir):
        Path.mkdir(test_dir)
