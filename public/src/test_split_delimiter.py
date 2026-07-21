import unittest
from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from text_to_textnode import text_to_textnode

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_text_to_textnode(self):
        new_nodes = text_to_textnode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(
                    [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], new_nodes,
        )

if __name__ == "__main__":
    unittest.main()





