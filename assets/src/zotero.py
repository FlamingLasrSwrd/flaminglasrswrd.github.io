import json

with open('zotero.json', 'r') as zotfile:
	bib = json.load(zotfile)

types = []
vars = []
for b in bib:
	for v in b.keys():
		if v not in vars:
			vars.append(v)
	if b['type'] not in types:
		types.append(b['type'])

vars = sorted(vars)
types = sorted(types)

# Generate type switch statement in fluid
for t in types:
	print('{% when "' + t + '" %}')

prepend = 'record'
# Generate assignment statements
for v in vars:
	print('{% assign ' + v + ' = ' + prepend + '.' + v + ' %}')

if __name__ == '__main__':
	
