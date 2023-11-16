from pathlib import Path


class TargetDirNotFoundError(Exception):
    """Raise when the target directory for the new project cannot be found."""


def new(target_dir, project_name):
    if not Path.exists(Path(target_dir)):
        raise TargetDirNotFoundError(f"Target directory '{target_dir}' not found")
    new_project_dir = Path(target_dir, project_name)
    if not Path.exists(new_project_dir):
        Path.mkdir(new_project_dir)

    source_dir = Path(new_project_dir, 'src')
    include_dir = Path(new_project_dir, 'src')
    if not Path.exists(source_dir):
        Path.mkdir(source_dir)
    if not Path.exists(include_dir):
        Path.mkdir(include_dir)
