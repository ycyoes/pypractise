items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)

x = {}
x[0] = 2
print(x)

y = x
x['key'] = 'value'
print(y)

b = {}.fromkeys(['name', 'age'])
print(b)

d = {}
print(d.get('name'))
print(d.get('name', 'N/A'))