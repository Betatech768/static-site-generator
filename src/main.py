import os
from pathlib import Path
from copy_to_public import clear_public, copy_to_public
from generate_page import generate_page


ROOT_DIR = Path(__file__).resolve().parents[1]
SOUCRE_DIR = os.path.join(ROOT_DIR, "static")
PUBLIC = os.path.join(ROOT_DIR, "public")


def main():
    if os.path.exists(PUBLIC):
        clear_public(PUBLIC)

    copy_to_public(SOUCRE_DIR, PUBLIC)

    CONTENT_PATH = os.path.join(ROOT_DIR, "content/index.md")
    TEMPLATE_PATH = os.path.join(ROOT_DIR, "template.html")
    DESTINATION_PATH = os.path.join(PUBLIC, "index.html")
    
    generate_page(CONTENT_PATH, TEMPLATE_PATH,  DESTINATION_PATH)




main()
