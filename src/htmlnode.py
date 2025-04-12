
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        print(f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}")

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        result = ""
        for k, v in self.props:
            result += f" {k}={v}"
        return result

