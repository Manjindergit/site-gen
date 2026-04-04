from src.functions.markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.functions.text_to_textnodes import text_to_textnodes
from src.textnode import text_node_to_html_node
from src.parentnode import ParentNode
from src.leafnode import LeafNode

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child = []
    for block in blocks:
        html_node = block_to_html_node(block)
        child.append(html_node)
    return ParentNode("div", child)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == BlockType.PARAGRAPH:
        return paraph_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    raise ValueError(f"Unknown block type: {block_type}")
    
def paraph_to_html_node(block):
    lines = block.split("\n")
    paragraph_text = " ".join(line.strip() for line in lines)
    return ParentNode("p", text_to_children(paragraph_text))
    
def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if (level + 1) > len(block):
        raise ValueError(f"Invalid heading block: {block}")
    heading_text = block[level + 1:].strip()
    return ParentNode(f"h{level}", text_to_children(heading_text))

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError(f"Invalid code block: {block}")
    code_text = block[4:-3].strip()
    raw_text_node = TextNode(code_text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    return ParentNode("pre", [ParentNode("code", [child])])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
