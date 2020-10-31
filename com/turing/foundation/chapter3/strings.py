format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)

from string import Template
tmpl = Template("hello, $who! $what enough for ya?")
tmpl.substitute(who='Mars', what='Dusty')
print(tmpl)

from math import e
a = f"Euler's constant is roughly {e}."
print(a)

fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for pi"
print(tmpl.format(mod=math))

print("The number is {num:b}".format(num=42))

print('One googol is {:,}'.format(10**100))

print("{:$^15}".format(" WIN BIG "))

import string 
print(string.capwords("that's all, folks"))

table = str.maketrans('cs', 'kz')
print(table)

print('this is an incredible test'.translate(table))