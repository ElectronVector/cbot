from pathlib import Path


def new(target_dir, project_name):
    new_project_folder = Path(target_dir, project_name)
    Path.mkdir(new_project_folder)
