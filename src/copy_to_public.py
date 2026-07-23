import os 
import shutil
from pathlib import Path


def clear_public(path):
    shutil.rmtree(path)

def copy_to_public(directory, destination):
    os.makedirs(destination, exist_ok=True)

    # Base Case 
    for dir in os.listdir(directory):
        src_path = os.path.join(directory, dir)
        dest_path = os.path.join(destination, dir)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            copy_to_public(src_path, dest_path)

