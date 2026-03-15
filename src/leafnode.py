from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        super().__init__(tag, value, None, props)
        
        
    def to_html(self):
        if not self.value:
            raise ValueError("Violate leafnode consraint")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HTMLNode: Tag:{self.tag} Value:{self.tag} Props:{self.props}"