from typing import Text

from textnode import TextNode, TextType
from helper import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_node = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_node.append(old_nodes)

        old_node_split: list[str] = old_node.text.split(delimiter)

        if len(old_node_split) % 2 == 0:
            raise ValueError("missing closing delimiter")

        for i, part in enumerate(old_node_split):
            if part == "":
                continue

            if i % 2 == 0:
                new_node.append(TextNode(part, TextType.TEXT))
            else:
                new_node.append(TextNode(part, text_type))

    return new_node


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_node: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_node.append(old_node)
        text = old_node.text

        image_node_list: list[tuple[str, str]] = extract_markdown_images(text)

        for image in image_node_list:
            image_alt = image[0]
            image_link = image[1]
            section = old_node.text.split(f"![{image_alt}]({image_link})", 1)
            if len(section) != 2:
                raise Exception("invalid markdown, image section not closed")
            if section[0] != "":
                new_node.append(TextNode(section[0], TextType.TEXT))
            new_node.append(TextNode(image_alt, TextType.IMAGE, image_link))
            old_nodes = section[1]
        if text != "":
            new_node.append(TextNode(text, TextType.TEXT))
    return new_node


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pass
