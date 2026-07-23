import os
from helper import markdown_to_html_node, extract_title


def generate_page(from_path: str, template_path:str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

   
    with open(from_path, "r") as f:
        content_of_markdown = f.read()

    
    with open(template_path, "r") as f:
        template_file_content = f.read()


    html_string = markdown_to_html_node(content_of_markdown).to_html()
    page_title = extract_title(content_of_markdown)


    template_file_content = (
                        template_file_content
                        .replace("{{ Title }}", page_title)
                        .replace("{{ Content }}", html_string)
                        )
    
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template_file_content)

