from pathlib import Path


def new(target_dir, project_name):
    new_project_folder = Path(target_dir, project_name)
    if not Path.exists(new_project_folder):
        Path.mkdir(new_project_folder)
