import unittest

from src.textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()