from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag, value, children=None, props=props)
    if value is None:
      raise ValueError
    
  def to_html(self):
    if self.value is None:
      raise ValueError
    if self.tag is None:
      return self.value
    props_html = self.props_to_html()
    return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
  