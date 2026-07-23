import os
from helper import markdown_to_html_node, extract_title


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, item)
        if os.path.isfile(file_path):

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
                template_path_content
                .replace("{{ Title }}", title)
                .replace("{{ Content }}", html_string)
                .replace('href="/', f'href="{basepath}')
                .replace('src="/', f'src="{basepath}')
            )

            with open(output_file_path, "w") as f:
                f.write(template_path_content)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item), basepath)
