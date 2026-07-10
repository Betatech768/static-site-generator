import unittest

from helper import extract_markdown_links, extract_markdown_images


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


if __name__ == "__main__":
    unittest.main()
