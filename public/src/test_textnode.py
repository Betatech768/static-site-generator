import unittest

from textnode import TextNode, TextType


class TestTexNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is Goodness", TextType.CODE)
        node2 = TextNode("This is John", TextType.PLAIN, "https://google.com")
        self.assertNotEqual(node, node2)

    if __name__ == "__main__":
        unittest.main()
