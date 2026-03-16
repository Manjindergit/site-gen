from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    
    def __init__(self, tag: str = None, children: list = None, props: dict = None):
        super().__init__(tag, None, children, props )
        
    def to_html(self):
        
        if not self.tag:
            raise ValueError("No Tag")
        if not self.children:
            raise ValueError("NO children")
        
        children_html = ""
        
        for child in self.children:
            children_html+=child.to_html()
            
        return f"<{self.tag}>{children_html}</{self.tag}>"
            