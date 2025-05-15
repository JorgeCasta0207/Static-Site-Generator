import unittest
from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter


class TestSplitDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        node = TextNode("Hello world", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Hello world")
        self.assertEqual(result[0].text_type, TextType.TEXT)
    
    def test_single_delimiter_pair(self):
        node = TextNode("Hello **world**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "world")
        self.assertEqual(result[1].text_type, TextType.BOLD)




if __name__ == "__main__":
    unittest.main()