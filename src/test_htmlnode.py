import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
  def test_to_html(self):
    self.assertRaises(NotImplementedError)
  
  def test_props_to_html(self):
    node = HTMLNode("link", "link", "a", {"href": "https://www.google.com", "target": "_blank"})
    self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
  unittest.main()