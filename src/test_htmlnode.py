import unittest

from htmlnode import HTMLNode

class testHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "Lorem Ipsum",
            None, 
            {"href": "https://www.google.com", "target": "_blank",}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_more_values(self):
        node = HTMLNode(
            "a",
            "this is random text",
            None,
            {"href": "https://www.youtube.com"}
        )
        self.assertEqual(
            node.tag,
            "a",
        )
        self.assertEqual(
            node.value,
            "this is random text",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            {"href": "https://www.youtube.com"},
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()