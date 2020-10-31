
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}
my_sister = 'Anne Lie Hetland'
storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('Lie', []).append(my_sister)
storage['last'].setdefault('Hetland', []).append(my_sister)

print(storage['first']['Anne'])
print(storage['middle']['Lie'])

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
MyNames = {}
# init(MyNames)
store(storage, 'Magnus Lie Hetland')

print(lookup(storage, 'middle', 'Lie'))

def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')

def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')

args = {'name': 'Mr. Gumby', 'age': 42}
with_stars(**args)
# print(with_stars(**args))
# print(without_stars(args))
without_stars(args)

def story(**kwds):
    return 'Once upon a time, there was a ' \
        '{job} called {name}.'.format_map(kwds)

def power(x, y, *others):
    if others:
        print('Received redundant parameters: ', others)
    return pow(x, y)

def interval(start, stop=None, step = 1):
    'Imitates range() for step > 0'
    if stop is None: 
        start, stop = 0, start
        result = []

        i = start 
        while i < stop:
            result.append(i)
            i += step
        return result

print(story(job='king', name='Gumby'))
print(story(job='brave knight', name='Sir Robin'))

params = {'job': 'language', 'name': 'Python'}
print(story(**params))

del params['job']
print(params)

print(story(job='stroke of genius', **params))

params = (5,) * 2
print(params)

print(power(*params))
print(*params)
print(power(5, 5))

print(power(3, 3, 'Hello, world'))

print(interval(10))