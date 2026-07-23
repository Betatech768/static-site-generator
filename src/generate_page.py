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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, item)
        if os.path.isfile(file_path):
            print(f"Generating page from {file_path} to {os.path.join(dest_dir_path, item)} using {template_path}")

            with open(file_path, "r") as f:
                markdown_content = f.read()
            
            with open(template_path, "r") as f:
                template_path_content = f.read()

            html_string = markdown_to_html_node(markdown_content).to_html()
            title = extract_title(markdown_content)

            output_filename = os.path.splitext(item)[0] + ".html"
            output_file_path = os.path.join(dest_dir_path, output_filename)
            os.makedirs(os.path.dirname(os.path.join(dest_dir_path, output_filename)), exist_ok=True)

            template_path_content = (
                template_path_content.replace("{{ Title }}", title)
                .replace("{{ Content }}", html_string)
            )

            with open(output_file_path, "w") as f:
                f.write(template_path_content)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item))
