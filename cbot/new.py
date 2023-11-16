from pathlib import Path


class TargetDirNotFoundError(Exception):
    """Raise when the target directory for the new project cannot be found."""


def new(target_dir, project_name):
    if not Path.exists(Path(target_dir)):
        raise TargetDirNotFoundError
    new_project_folder = Path(target_dir, project_name)
    if not Path.exists(new_project_folder):
        Path.mkdir(new_project_folder)
