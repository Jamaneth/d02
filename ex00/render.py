import re
import sys

from settings import *

def template_name():

    if len(sys.argv) != 2:
        raise TypeError("Only one positional argument expected")

    elif sys.argv[1].split('.')[-1] != "template":
        raise TypeError("Wrong file extension")

    else:
        return sys.argv[1]

def render_function():
    # ERROR MANAGEMENT STILL TO DO (but how to make it work?)
    file = open(template_name(), 'r')
    html_text = file.read()
    html_output = open('myCV.html', 'w')

    for variable in globals().keys():
        # globals().keys() gives us the full list of variables, including those in the settings.py
        # document.
        # We therefore try to match those variables with the variables in the template.
        print(variable)
        if "{" + variable + "}" in html_text:

            html_text = re.sub("{" + variable + "}", str(globals()[variable]), html_text)

    html_output.write(html_text)
    return html_text

if __name__ == '__main__':

    render_function()
