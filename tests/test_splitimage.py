import unittest
from src.textnode import TextNode, TextType
from src.functions.splitnodes import split_nodes_image, split_nodes_link

class TestSplitNodesImage(unittest.TestCase):

    def test_single_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and more",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertEqual(result, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and more", TextType.TEXT),
        ])

    def test_two_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertEqual(result, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ])

    def test_image_at_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) some text after",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertEqual(result, [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" some text after", TextType.TEXT),
        ])

    def test_image_at_end(self):
        node = TextNode(
            "some text before ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertEqual(result, [
            TextNode("some text before ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ])

    def test_no_image(self):
        node = TextNode("just plain text", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [TextNode("just plain text", TextType.TEXT)])

    def test_non_text_node_passes_through(self):
        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_image([node])
        self.assertEqual(result, [TextNode("already bold", TextType.BOLD)])

    def test_mixed_list(self):
        nodes = [
            TextNode("text with ![img](https://img.png) here", TextType.TEXT),
            TextNode("already italic", TextType.ITALIC),
        ]
        result = split_nodes_image(nodes)
        self.assertEqual(result, [
            TextNode("text with ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://img.png"),
            TextNode(" here", TextType.TEXT),
            TextNode("already italic", TextType.ITALIC),
        ])


class TestSplitNodesLink(unittest.TestCase):

    def test_single_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) here",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertEqual(result, [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" here", TextType.TEXT),
        ])

    def test_two_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertEqual(result, [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ])

    def test_link_at_start(self):
        node = TextNode(
            "[click here](https://www.boot.dev) some text after",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertEqual(result, [
            TextNode("click here", TextType.LINK, "https://www.boot.dev"),
            TextNode(" some text after", TextType.TEXT),
        ])

    def test_link_at_end(self):
        node = TextNode(
            "some text before [click here](https://www.boot.dev)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertEqual(result, [
            TextNode("some text before ", TextType.TEXT),
            TextNode("click here", TextType.LINK, "https://www.boot.dev"),
        ])

    def test_no_link(self):
        node = TextNode("just plain text", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [TextNode("just plain text", TextType.TEXT)])

    def test_non_text_node_passes_through(self):
        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_link([node])
        self.assertEqual(result, [TextNode("already bold", TextType.BOLD)])

    def test_image_not_matched_as_link(self):
        node = TextNode("just plain text with no links", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [TextNode("just plain text with no links", TextType.TEXT)])

    def test_mixed_list(self):
        nodes = [
            TextNode("text with [link](https://boot.dev) here", TextType.TEXT),
            TextNode("already code", TextType.CODE),
        ]
        result = split_nodes_link(nodes)
        self.assertEqual(result, [
            TextNode("text with ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" here", TextType.TEXT),
            TextNode("already code", TextType.CODE),
        ])


if __name__ == "__main__":
    unittest.main()