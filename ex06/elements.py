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
        self.tag = "h2"
        self.tag_type = "double"
        super().__init__(self.tag, attr, content, self.tag_type)

class P(Elem):

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


def test_basic():

    assert str(Html()) == '<html></html>'
    assert str(Head()) == '<head></head>'
    assert str(Body()) == '<body></body>'
    assert str(Html([Head(), Body()])) == '<html>\n  <head></head>\n  <body></body>\n</html>'
    assert str(Title(Text('Test'))) == '<title>\n  Test\n</title>'
    assert str(Meta()) == '<meta />'
    assert str(Img()) == '<img />'
    assert str(Img(attr = {'src': 'http://i.imgur.com/pfp3T.jpg'})) == '<img src="http://i.imgur.com/pfp3T.jpg" />'
    assert str(Table([Tr(), Tr()])) == '<table>\n  <tr></tr>\n  <tr></tr>\n</table>'
    assert str(Th()) == '<th></th>'
    assert str(Td()) == '<td></td>'
    assert str(Ul()) == '<ul></ul>'
    assert str(Ol()) == '<ol></ol>'
    assert str(Li()) == '<li></li>'
    assert str(Body([H1(Text('Test')), H2(Text('Test'))])) == '<body>\n  <h1>\n    Test\n  </h1>\n  <h2>\n    Test\n  </h2>\n</body>'
    assert str(P(Text('Test'))) == '<p>\n  Test\n</p>'
    assert str(Div()) == '<div></div>'
    assert str(Span()) == '<span></span>'
    assert str(Hr()) == '<hr />'
    assert str(Br()) == '<br />'

    print('Functionality: OK')


if __name__ == '__main__':

    print(str(Body([H1(Text('Test')), H2(Text('Test'))])))
    test_basic()

    html_text = Html([Head(Title(Text("Hello ground!"))),
    Body([H1(Text("Oh no, not again!")), Img(attr = {'src': 'http://i.imgur.com/pfp3T.jpg'})])])

    print(html_text)
