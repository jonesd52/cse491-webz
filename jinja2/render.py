import jinja2
import sys

# this sets up jinja2 to load templates from the 'templates' directory
loader = jinja2.FileSystemLoader('./templates')
env = jinja2.Environment(loader=loader)

# pick up a filename to render
filename = sys.argv[1]
print >>sys.stderr, '** Rendering:', filename

# variables for the template rendering engine
vars = dict(firstname='Zippy', lastname='Longstocking')
print >>sys.stderr, "** Using vars dictionary:", vars

template = env.get_template(filename)
print template.render(vars)
