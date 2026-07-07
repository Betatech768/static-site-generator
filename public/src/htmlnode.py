class HTMLNode:
    def __init__(
        self,
        tag: str = "",
        value: str = "",
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
