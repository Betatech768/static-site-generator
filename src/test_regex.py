import unittest

from helper import (
    extract_markdown_links,
    extract_markdown_images,
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)


class TestExtractImagesAndLink(unittest.TestCase):
    def test_regex_result(self):
        node = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            node,
        )

    def test_regex_link(self):
        node = extract_markdown_links("[to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], node)

    def test_markdown_to_block(self):
        markdown = """
                        This is **bolded** paragraph

                        This is another paragraph with _italic_ text and `code` here
                        This is the same paragraph on a new line

                        - This is a list
                        - with items
                    """

        node = markdown_to_blocks(markdown)

        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            node,
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
