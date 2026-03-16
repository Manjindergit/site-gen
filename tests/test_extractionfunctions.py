import unittest
from src.functions.extractmdimg import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        markdown_text = "Here is an image: ![Alt text](https://example.com/image.png) and another one ![Another image](https://example.com/another-image.jpg)"
        expected_output = [
            ("Alt text", "https://example.com/image.png"),
            ("Another image", "https://example.com/another-image.jpg")
        ]
        self.assertEqual(extract_markdown_images(markdown_text), expected_output)
        
    def test_extract_markdown_links(self):
        markdown_text = "Here is a link: [Google](https://www.google.com) and another one [GitHub](https://github.com)"
        expected_output = [
            ("Google", "https://www.google.com"),
            ("GitHub", "https://github.com")
        ]
        self.assertEqual(extract_markdown_links(markdown_text), expected_output)    
            
class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        markdown_text = "Here is a link: [Google](https://www.google.com) and another one [GitHub](https://github.com)"
        expected_output = [
            ("Google", "https://www.google.com"),
            ("GitHub", "https://github.com")
        ]
        self.assertEqual(extract_markdown_links(markdown_text), expected_output)
        
    def test_extract_markdown_images(self):
        markdown_text = "Here is an image: ![Alt text](https://example.com/image.png) and another one ![Another image](https://example.com/another-image.jpg)"
        expected_output = [
            ("Alt text", "https://example.com/image.png"),
            ("Another image", "https://example.com/another-image.jpg")
        ]
        self.assertEqual(extract_markdown_images(markdown_text), expected_output)