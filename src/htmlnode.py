from typing import override


class HTMLNode:
    def __init__(
        self,
        tag: str = "",
        value: str = "",
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag: str = tag
        self.value: str = value
        self.children: list["HTMLNode"] | None = children
        self.props: dict[str, str] | None = props

    def to_html(self) -> str:

        raise NotImplementedError("Method or Function hasn't been implemented yet")

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        formatted_value = ""
        for key, value in self.props.items():
            formatted_value += f' {key}="{value}"'

        return formatted_value

    @override
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag!r}, {self.value!r})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None):
        super().__init__(tag=tag, value=value, children=[], props=props)

    @override
    def to_html(self):
        if self.value is None:
            raise ValueError("inappropraite value or type")

        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    @override
    def __repr__(self):
        return f" LeafNode({self.tag!r}, {self.value!r})"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode] | None,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag=tag, children=children, props=props)

    @override
    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("tag is required")

        if self.children is None:
            raise ValueError("Children is Required")

        html_children = ""

        for child in self.children:
            print(child)
            html_children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"

    @override
    def __repr__(self) -> str:
        return f"ParentNode({self.tag!r}, children: {self.children!r}, {self.props!r})"
