import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node.text, node2.text)
    
    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)


    def test_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://thenewstore.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://chickenwing.aol")
        self.assertNotEqual(node.url, node2.url)

 
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertIsNone(node.url)




if __name__ == "__main__":
    unittest.main()
