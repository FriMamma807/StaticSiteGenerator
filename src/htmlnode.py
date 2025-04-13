
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
        if self.props is not None:
            result = ""
            for key in self.props:
                result += f" {key}={self.props[key]}"
            return result
        else:
            return None




