from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = HTMLNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    
if __name__ == "__main__":
    main()
    
    