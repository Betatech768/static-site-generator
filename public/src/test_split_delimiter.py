import unittest
from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter


class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter(self):
        node = split_nodes_delimiter(
            [TextNode("this should bolden *this text*", TextType.TEXT)],
            "*",
            TextType.BOLD,
        )
        node2 = [
            TextNode("this should bolden ", TextType.TEXT),
            TextNode("this text", TextType.BOLD),
        ]

        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
