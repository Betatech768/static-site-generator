import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("Bold", "Greatness", ["str", "bell"])
        node2 = HTMLNode("Bold", "Greatness", ["str", "bell"], {"arsg": "game"})

        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), f' arsg="game"')


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "grace to go on")
        node2 = LeafNode("a", "Check Me Out!", {"href": "https://boot.dev"})
        node4 = LeafNode(None, "Hello John")

        self.assertEqual(node4.to_html(), "Hello John")

        with self.assertRaises(ValueError):
            LeafNode("a", None).to_html()

        self.assertEqual(node.to_html(), "<p>grace to go on</p>")
        self.assertEqual(
            node2.to_html(), '<a href="https://boot.dev">Check Me Out!</a>'
        )


if __name__ == "__main__":
    unittest.main()
