import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()