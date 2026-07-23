import re

def extract_markdown_images(text) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text) -> list[tuple[str, str]]:
    matches: list[tuple[str, str]] = re.findall(r"\[(.*?)\]\((.*?)\)", text)

    return matches
