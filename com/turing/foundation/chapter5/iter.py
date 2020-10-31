names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')

print(list(zip(names, ages)))

print(list(zip(range(5), range(100000000))))

print(sorted('aBc', key=str.lower))

from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
    # print(letterGirls)
    # print([b+'+'+ g for b in boys for g in letterGirls[b[0]]])
    for b in boys:
        if b[0] in letterGirls: 
            print(b, letterGirls[b[0]])


scope = {}
print(exec('x=2', scope))
print(eval('x*x', scope))

import math
x = 1
y = math.sqrt
print(callable(x))
