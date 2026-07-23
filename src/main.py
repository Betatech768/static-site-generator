import os 
import shutil
from pathlib import Path



ROOT_DIR = Path(__file__).resolve().parents[1]
SOUCRE_DIR = os.path.join(ROOT_DIR, "static")
PUBLIC = os.path.join(ROOT_DIR, "public")

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


def main():
    if os.path.exists(PUBLIC):
        clear_public(PUBLIC)

    copy_to_public(SOUCRE_DIR, PUBLIC)


main()
