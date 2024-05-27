import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
  def test_no_tag(self):
    try:
      node = ParentNode(children=[LeafNode("p", "Child Node")])
      self.assertRaises(ValueError)
    except ValueError:
      pass

  def test_no_children(self):
    try:
      node = ParentNode("div")
      self.assertRaises(ValueError)
    except ValueError:
      pass

  def test_children(self):
    node = ParentNode("p", [LeafNode("b", "Bold text"),
                            LeafNode(None, "Normal text"),
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                            ])
    expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    self.assertEqual(node.to_html(), expected_result)

if __name__ == "__main__":
  unittest.main()