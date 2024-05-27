class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")

  # Naive approach
  # def props_to_html(self):
  #   html_string = ""
  #   for key, val in self.props.items():
  #     html_string += str(key)
  #     html_string += "="
  #     html_string += "\""
  #     html_string += str(val)
  #     html_string += "\""
  #     html_string += " "
  #   return html_string

  def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
  
  def __repr__(self) -> str:
    return f"tag: {self.tag}, val: {self.value}, children: {self.children}, props: {self.props}"