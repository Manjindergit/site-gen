from src.textnode import TextType, TextNode
from src.functions.extractmdimg import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid markdown syntax")
        for i, text in enumerate(split_text):
            if text == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        
        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        remaining = node.text
        for alt, url in images:
            sections = remaining.split(f"![{alt}]({url})", 1)
            if sections[0]!="":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            remaining = sections[1]
            
        if remaining!="":
            new_nodes.append(TextNode(remaining, TextType.TEXT))
            
    return new_nodes
        

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type!=TextType.TEXT:
            new_nodes.append(node)
            continue
    
        links = extract_markdown_links(node.text)
        
        if len(links)==0:
            new_nodes.append(node)
            continue
        
        remaining = node.text
        
        for name, link in links:
            sections = remaining.split(f"[{name}]({link})", 1)
            if sections[0]!="":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(name, TextType.LINK, link))
            remaining = sections[1]
            
        if remaining!="":
            new_nodes.append(TextNode(remaining, TextType.TEXT))
            
    return new_nodes
            
        
            
        