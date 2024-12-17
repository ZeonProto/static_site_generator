import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false_text(self):
        node = TextNode("My Text is shorter", TextType.ITALIC)
        node2 = TextNode("My Text is waaaaaaaaaaaaaaaaay longer", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_false_url(self):
        node = TextNode("Hello world", TextType.CODE, "https://www.youtube.com")
        node2 = TextNode("Hello world", TextType.CODE, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is the same text", TextType.CODE, "https://www.youtube.com")
        node2 = TextNode("This is the same text", TextType.CODE, "https://www.youtube.com")
        self.assertEqual(node, node2)

    def test_eq_false_TextType(self):
        node = TextNode("This Text is Text :)", TextType.BOLD)
        node2 = TextNode("This Text is Text :)", TextType.ITALIC)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is text")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src" : "https://www.image.com", "alt" : "This is an image"}
        )

    def test_italic(self):
        node = TextNode("This text is slanted", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This text is slanted")

if __name__ == "__main__":
    unittest.main()