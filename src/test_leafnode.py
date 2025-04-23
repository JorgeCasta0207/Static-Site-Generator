import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")



    def test_leaf_with_props(self):
        node = LeafNode("p", "Hello World!", props={"img": "hello.jpg"})
        self.assertEqual(node.to_html(), '<p img="hello.jpg">Hello World!</p>')



    def test_leaf_no_value(self):
        node = LeafNode("p", "")

        with self.assertRaises(ValueError) as context:
            node.to_html()

    def test_leaf_no_tag(self):
        node = LeafNode("", "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")



if __name__ == "__main__":
    unittest.main()
