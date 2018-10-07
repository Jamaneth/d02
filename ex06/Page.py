from elements import *

class Page():
    """
    In order to tackle the problem, I represented the nested elements in a tree.
    The key represents the position in the tree according to the starting point: for
    instance, '0,0,1' would refer to the 1st child of the 0th chlid of the 0th source node.

    The according value in the dictionary is the tag associated with that particular node.
    """
    def __init__(self, elem):

        assert str(elem)
        self.elem = elem

        self.tree = Page.__tree_definition(self, elem, key = '')

    def __tree_definition(self, elem, key = ''):

        tree = dict()

        if Elem.check_type(elem):

            if type(elem) == list:
                for ind in range(0, len(elem)):
                    tree[key + str(ind)] = elem[ind].tag
                    if len(key) > 0:
                        tree = {**tree, **Page.__tree_definition(self, elem[ind], key + ',' + str(ind))}
                    else:
                        tree = {**tree, **Page.__tree_definition(self, elem[ind], str(ind))}

            elif type(elem.content) == list and Elem.check_type(elem.content):
                if len(key) == 0: key = '0'
                tree[key] = elem.tag
                for ind in range(0, len(elem.content)):
                    if isinstance(elem.content[ind], Elem):
                        tree = {**tree, **Page.__tree_definition(self, elem.content[ind], key + ',' + str(ind))}
                    elif isinstance(elem.content[ind], Text):
                        tree[key + ',' + str(ind)] = 'text'

            elif isinstance(elem.content, Elem):
                if len(key) == 0: key = '0'
                tree[key] = elem.tag
                tree = {**tree, **Page.__tree_definition(self, elem.content, key + ',0')}

            elif isinstance(elem.content, Text):
                tree[key] = 'text'
                return tree

            else:
                if len(key) == 0: key = '0'
                tree[key] = elem.tag
                return tree

        else:
            raise Elem.ValidationError

        return tree

    def __str__(self):

        if self.tree['0'] == 'html':
            return '<!DOCTYPE html>\n\n' + str(self.elem)
        else:
            return str(self.elem)


    def get_children(self, node_searched):

        node_depth = node_searched.count(',') # Number of commas can determine the depth of the node we search
        children = {}

        for node, tag in self.tree.items():
            if node.startswith(node_searched) and node.count(',') == node_depth + 1:
                children[node] = tag

        return children

    def is_valid(self):

        def tag_test(self, tag):
            return (tag in {'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr',
            'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br', 'text'})


        def html_test(self, node, tag, children):
            if tag == 'html':
                if len(children.keys()) == 2:
                    return (children[node + ',0'] == 'head' and children[node + ',1'] == 'body')
                else:
                    return False
            else:
                return True

        def head_test(self, node, tag, children):
            if tag == 'head':
                return(len(children) <= 1 and set(children.values()).issubset({'title'}))
            else:
                return True

        def body_div_test(self, node, tag, children):
            if tag == "body" or tag == "div":
                return set(children.values()).issubset({'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'text'})
            else:
                return True

        def unique_text_test(self, node, tag, children):
            if tag in ("title", "h1", "h2", "li", "th", "td"):
                return len(children.values()) <= 1 and set(children.values()).issubset({"text"})
            else:
                return True

        def p_test(self, node, tag, children):
            if tag == "p":
                return set(children.values()).issubset({"text"})
            else:
                return True

        def span_test(self, node, tag, children):
            if tag == "span":
                return set(children.values()).issubset({"text", "p"})
            else:
                return True

        def ul_ol_test(self, node, tag, children):
            if tag == "ul" or tag == "ol":
                return len(children.values()) > 0 and set(children.values()).issubset({"li"})
            else:
                return True

        def tr_test(self, node, tag, children):
            if tag == "tr":
                return len(set(children.values())) == 1 and set(children.values()).issubset({"th", "td"})
            else:
                return True

        def table_test(self, node, tag, children):
            if tag == "table":
                return set(children.values()).issubset({"tr"})

        for node, tag in self.tree.items():

            children = self.get_children(node)
            tests = {
            'tag_test': tag_test(self, tag),
            'html_test': html_test(self, node, tag, children),
            'head_test': head_test(self, node, tag, children),
            'body_div_test': body_div_test(self, node, tag, children),
            'unique_text_test': unique_text_test(self, node, tag, children),
            'p_test': p_test(self, node, tag, children),
            'span_test': span_test(self, node, tag, children),
            'ul_ol_test': ul_ol_test(self, node, tag, children),
            'tr_test': tr_test(self, node, tag, children),
            'table_test': table_test(self, node, tag, children)
            }

            for key, value in tests.items():
                if value == False:
                    #print('Problem with ' + key)
                    #print(node + ' - ' + tag)
                    return False

        else:
            return True


def validity_test():

    assert Page(Html([Head(), Body()])).is_valid() == True
    assert Page(Head(Title())).is_valid() == True
    assert Page([Body([H1(), H2(), Span()]), Div([H1(), H2()])]).is_valid() == True
    assert Page(P(Text('Test'))).is_valid() == True
    assert Page(Span([Text('Test'), P()])).is_valid() == True
    assert Page([Ul(Li()), Ul([Li(), Li()]), Ol(Li())]).is_valid() == True
    assert Page([Tr(Th()), Tr([Td(), Td()])]).is_valid() == True
    assert Page(Table([Tr(Th()), Tr([Td(), Td()])])).is_valid() == True
    print('Rule validation: OK')


def not_valid_test():

    assert Page(Html([Head(), Body(), Span()])).is_valid() == False # Too many elements
    assert Page(Html([Head()])).is_valid() == False # Not enough
    assert Page(Html([Head(), Span()])).is_valid() == False # Wrong elements

    assert Page(Head([Title(), Title()])).is_valid() == False # Two titles
    assert Page(Head([Title(), Span()])).is_valid() == False # Another element
    assert Page(Head(Span())).is_valid() == False # Wrong element

    assert Page(Body(P())).is_valid() == False # Wrong element

    assert Page(Title([Text('Test'), Text('Test')])).is_valid() == False # Two texts
    assert Page(Title([Text('Test'), Span(Text('Test'))])).is_valid() == False # Non-text element

    assert Page(P([Text('Test'), Span(Text('Test'))])).is_valid() == False # Non-text element

    assert Page(Span([Text('Test'), Div(Text('Test'))])).is_valid() == False # Non-text element

    assert Page(Ul()).is_valid() == False # Check emptiness
    assert Page(Ul([Li(), Text('Test')])).is_valid() == False # Wrong element

    assert Page(Tr()).is_valid() == False # Check emptiness
    assert Page(Tr([Td(), Th()])).is_valid() == False # Th and Td must be mutually exclusive
    assert Page(Tr([Td(), Td(), P()])).is_valid() == False # Wrong element

    assert Page(Table([Tr(), P()])).is_valid() == False # Wrong element
    print('Invalid outputs: OK')


if __name__ == '__main__':

    validity_test()
    not_valid_test()
