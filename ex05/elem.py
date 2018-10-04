#!/usr/bin/python3
# coding: utf-8

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.
    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        I added a few other replacements for the HTML escape characters.
        """
        return (
        super().__str__().replace('&', '&amp;')
        .replace('"', '&quot;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('\n', '\n<br />\n')
        )



class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.
        Obviously.
        """
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type

        if isinstance(content, Elem) or isinstance(content, Text):
            self.content = [content]
        elif isinstance(content, str) or isinstance(content, int):
            raise Elem.ValidationError
        else:
            self.content = content

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = '<' + self.tag + self.__make_attr() + ">"
            result += self.__make_content()
            result += '</' + self.tag + '>'

        elif self.tag_type == 'simple':
            result = '<' + self.tag + self.__make_attr() + " />"
            result += self.__make_content()
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """
        if self.content == None:
            return ''

        elif not Elem.check_type(self.content):
            raise Elem.ValidationError

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            elem = str(elem).split('\n')
            result += ''.join(['  ' + str(line) +  '\n' for line in elem if line != ''])

        if result == '\n':
            return ''
        else:
            return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

    class ValidationError(Exception):
        def __init__(self):
            Exception.__init__(self, "Wrong type of content (choose Text or Elem type).")


if __name__ == '__main__':

    html_page = Elem(tag = 'html',
    content = [Elem(tag = 'head', content = Elem(tag = 'title', content = Text('Hello ground!'))),
    Elem(tag = 'body', content = [Elem('h1', content = Text('Oh no, not again!')),
                                  Elem('img', attr = {'src': "http://i.imgur.com/pfp3T.jpg"}, tag_type = "simple")])])

    print(html_page)
