from os.path import join, split
from os import makedirs
from typing import Tuple
from glob import glob
from shutil import copytree

def get_path_and_filename(path: str) -> Tuple[str, str]:
    return split(path)

def get_filename(path: str):
    return get_path_and_filename(path)[1]

def get_path(path: str) -> str:
    return get_path_and_filename(path)[0]

def mkdir(path: str): 
    makedirs(path, exist_ok=True)

def get_all_files_in_dir(path: str):
    return list(glob(join(path, "*")))

def copy_dir(src: str, dst: str):
    copytree(src, dst)