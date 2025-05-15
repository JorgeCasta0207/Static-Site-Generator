import unittest
from htmlnode import ParentNode, LeafNode



class TestParentNode(unittest.TestCase):

    # Passed
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    

   # Passed
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )


    def test_props_provided(self):
        child_node = LeafNode("p", "child")
        parent_node = ParentNode("div", [child_node], props={"img": "hello.jpg"})
        
        self.assertEqual(
            parent_node.to_html(),
            '<div img="hello.jpg"><p>child</p></div>'
        )
    
    def test_no_props_provided(self):
        child_node = LeafNode("p", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            '<div><p>child</p></div>'
        )
        
        
    def test_no_tag_value_provided(self):
        child_node = LeafNode("", "child")
        parent_node = ParentNode("", [child_node])

        with self.assertRaises(ValueError) as context:
            parent_node.to_html()


    def test_no_children_provided(self):
        parent_node = ParentNode("div", "")

        with self.assertRaises(ValueError) as context:
            parent_node.to_html()


    








if __name__ == "__main__":
    unittest.main()