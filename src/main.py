import os
from pathlib import Path
from copy_to_public import clear_public, copy_to_public
from generate_page import generate_pages_recursive
import sys


ROOT_DIR = Path(__file__).resolve().parents[1]
SOUCRE_DIR = os.path.join(ROOT_DIR, "static")
PUBLIC = os.path.join(ROOT_DIR, "docs")
BASE_PATH = sys.argv[1] if len(sys.argv) > 1 else "/"

def main():
    if os.path.exists(PUBLIC):
        clear_public(PUBLIC)

    copy_to_public(SOUCRE_DIR, PUBLIC)

    CONTENT_PATH = os.path.join(ROOT_DIR, "content")
    TEMPLATE_PATH = os.path.join(ROOT_DIR, "template.html")
    DESTINATION_PATH = PUBLIC
    
    generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH,  DESTINATION_PATH, BASE_PATH)




main()
