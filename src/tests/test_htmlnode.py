import unittest
from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):



    def test_empty_property(self):
        node = HTMLNode(tag="div", props={})
        result = node.props_to_html()
        expected = ''
        self.assertEqual(result, expected)        


    def test_single_property(self):
        node = HTMLNode(tag="div", props={"id": "main"})
        result = node.props_to_html()
        expected = 'id="main"'
        self.assertEqual(result, expected)

    

    def test_multiple_properties(self):
        node = HTMLNode(tag="div", props={"id": "main", "href": "https://datest.aol", "title": "The Title"})
        result = node.props_to_html()
        self.assertIn('id="main"', result)
        self.assertIn('href="https://datest.aol"', result)
        self.assertIn('title="The Title"', result )


    
    






if __name__ == "__main__":
    unittest.main()