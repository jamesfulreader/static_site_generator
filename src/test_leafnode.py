import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_no_value(self):
    try:
      node = LeafNode("p")
      self.assertFalse(node, "Leaf node should raise Val Err if val not passed in or equals None")
    except ValueError:
      pass

  def test_no_tag(self):
    node = LeafNode(value="Test to test with")
    self.assertEqual(node.to_html(), "Test to test with")

  def test_tag(self):
    node = LeafNode("p", "p tag with text to be displayed inside")
    self.assertEqual(node.to_html(), "<p>p tag with text to be displayed inside</p>")
  
  def test_tag_props(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
  unittest.main()