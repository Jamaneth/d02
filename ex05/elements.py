from elem import Text, Elem

class Html(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "html"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Head(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "head"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Body(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "body"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Title(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "title"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Meta(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "meta"
        self.tag_type = "simple"
        super().__init__(self.tag, attr, content, self.tag_type)

class Img(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "img"
        self.tag_type = "simple"
        super().__init__(self.tag, attr, content, self.tag_type)

class Table(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "table"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Table(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "table"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Table(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "table"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Th(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "th"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Td(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "td"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Tr(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "tr"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Ul(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "ul"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Ol(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "ol"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Li(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "li"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class H1(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "h1"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class H2(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "H2"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class p(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "p"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Div(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "div"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Span(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "span"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class Hr(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "hr"
        self.tag_type = "simple"
        super().__init__(self.tag, attr, content, self.tag_type)

class Br(Elem):

    def __init__(self, content = None, attr = {}):
        self.tag = "br"
        self.tag_type = "simple"
        super().__init__(self.tag, attr, content, self.tag_type)

if __name__ == '__main__':

    html_text = Html([Head(Title(Text("Hello ground!"))),
    Body([H1(Text("Oh no, not again!")), Img(attr = {'src': 'http://i.imgur.com/pfp3T.jpg'})])])


    print(html_text)
