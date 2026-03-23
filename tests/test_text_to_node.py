import unittest
from src.textnode import TextNode, TextType
from src.functions.text_to_textnodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):

    def test_all_types(self):
        nodes = text_to_textnodes(
            "This is **bold** and _italic_ and `code` and ![image](https://img.png) and [link](https://boot.dev)"
        )
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://img.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], nodes)

    def test_plain_text(self):
        nodes = text_to_textnodes("just plain text")
        self.assertListEqual([
            TextNode("just plain text", TextType.TEXT),
        ], nodes)

    def test_bold_only(self):
        nodes = text_to_textnodes("**bold**")
        self.assertListEqual([
            TextNode("bold", TextType.BOLD),
        ], nodes)

    def test_italic_only(self):
        nodes = text_to_textnodes("_italic_")
        self.assertListEqual([
            TextNode("italic", TextType.ITALIC),
        ], nodes)

    def test_code_only(self):
        nodes = text_to_textnodes("`code`")
        self.assertListEqual([
            TextNode("code", TextType.CODE),
        ], nodes)

    def test_image_only(self):
        nodes = text_to_textnodes("![alt](https://img.png)")
        self.assertListEqual([
            TextNode("alt", TextType.IMAGE, "https://img.png"),
        ], nodes)

    def test_link_only(self):
        nodes = text_to_textnodes("[click](https://boot.dev)")
        self.assertListEqual([
            TextNode("click", TextType.LINK, "https://boot.dev"),
        ], nodes)

    def test_multiple_bold(self):
        nodes = text_to_textnodes("**one** and **two**")
        self.assertListEqual([
            TextNode("one", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
        ], nodes)

    def test_bold_and_italic(self):
        nodes = text_to_textnodes("**bold** and _italic_")
        self.assertListEqual([
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ], nodes)

    def test_image_and_link(self):
        nodes = text_to_textnodes(
            "![img](https://img.png) and [link](https://boot.dev)"
        )
        self.assertListEqual([
            TextNode("img", TextType.IMAGE, "https://img.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], nodes)

    def test_invalid_markdown_raises(self):
        with self.assertRaises(ValueError):
            text_to_textnodes("this is **unclosed bold")

if __name__ == "__main__":
    unittest.main()