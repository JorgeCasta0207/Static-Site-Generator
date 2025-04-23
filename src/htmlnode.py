

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}


    def to_html(self):
        raise NotImplementedError
    

    def props_to_html(self):
        if not self.props:
            return ''
        return ''.join(f'{key}="{value}"' for key, value in self.props.items()) 
    

    def __repr__(self):
        return f"HTMLNode(Tag={self.tag}, Value={self.value}, Children={self.children}, Props={self.props})"



class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=(), props=props)
        
    
    # Turning into HTML tag
    def to_html(self):
        if self.value is "" or self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        if self.tag == "" or self.tag is None:
            return self.value
        
        props_html = self.props_to_html()

        # Handling with and without attributes(props) cases
        if props_html:
            html_tag = f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        else:
            html_tag = f"<{self.tag}>{self.value}</{self.tag}>"

        return html_tag



    
