import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    
    def test_textnode_equality(self):
        node1 = TextNode("Hello World", TextType.TEXT)
        node2 = TextNode("Hello World", TextType.TEXT)
        self.assertEqual(node1, node2)
        
    def test_textnode_inequality(self):
        node1 = TextNode("Hello World", TextType.TEXT)
        node2 = TextNode("Hello World", TextType.BOLD)
        self.assertNotEqual(node1, node2)
        
    def test_textnode_repr(self):
        node = TextNode("Hello World", TextType.TEXT)
        expected_repr = "TextNode(text='Hello World', text_type='text', url='None')"
        self.assertEqual(repr(node), expected_repr)
        
    def test_textnode_with_url(self):
        node = TextNode("Click here", TextType.LINK, "https://www.example.com")
        expected_repr = "TextNode(text='Click here', text_type='link', url='https://www.example.com')"
        self.assertEqual(repr(node), expected_repr)
        
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()