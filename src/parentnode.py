from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag=None, children=None, props=None):
    super().__init__(tag, value=None, children=children, props=props)
    if children is None:
      raise ValueError
    
  def to_html(self):
    if self.tag is None:
      raise ValueError
    
    if not self.children:
      raise ValueError
    
    props_html = self.props_to_html()
    children_html = "".join(child.to_html() for child in self.children)
    return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
