from jinja2 import Template

template = Template("interface {{int}}\n shutdown")

for x in range(1,11):
	print( template.render(int = "Ethernet %s"%x))
