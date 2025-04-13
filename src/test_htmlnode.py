import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_node_props_with_value(self):
        node1 = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node1.props_to_html(), " href=https://www.google.com target=_blank")

    def test_html_to_props_default(self):
        node1=HTMLNode()
        self.assertEqual(node1.props_to_html(), None)

    def test_to_html_exception(self):
        node1 = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node1.to_html()



if __name__ == "__main__":
    unittest.main()