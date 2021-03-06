
def myfunc(a:float, *args, **kwargs) -> str:
    return str(a)

import numpy as np

x = np.array([1, 1])
print(myfunc(x))

def mysum(*args):
    result = 0
    for x in args:
        result += x
    return result
print(mysum(1,2,3))
print(mysum(2,3,5,6))

def my_concat(**kwargs):
    result = ""
    for k, v in kwargs.items():
        result += v
    return result
print(my_concat(x="a", y="b"))
# print(my_concat(fff=1, bsr="b"))

# The most commonly used ways for exception handling is to raise an exception (also called throw).
def raise_exception(x):
    raise Exception("I am an Exception!!!") #Something bad has happend
def catcher(x):
    try:
        raise_exception(x) # This will run the code. If everything is fine, it will return normally.
    except(TypeError, NameError):   #If a specific error occurs, this will follow the behavior.
        print("I am ok with this!")
    except Exception as e:  # This is often used to handle unknown exception,by letting someone else do the job
        raise e
    finally: #This will always execute no matter what
        print("Let us swallow everything when exception occurs!")

# print(catcher(1))

# There are quite some problem with the following approach.
    # It breaks the program, as long as one exception is not handled.
    # This is ok if we are testing our code. However, if this is a production system, you don't want a night time call to restart the system.
    # Once one function throws an exception, everyone else that calls the function has to modify their code by addding try-except blocks.
    # Many exception will be passed all the way to the top, and then handled. However, the top function does not know the details of each function! Therefore, it is extremely hard to devise a complete plan.

# An alternative way is to use log. There are many logging options and we will not delve into the details. The idiom is to log what goes wrong and specify the bevahior.

# The advantage is that you will keep the program warning, and by adjusting the log level, you can adjust the behavior. However, someone still have to handle the exceptions!

import logging
logging.info("This is some useful information.")
logging.warning("This is some warning!")
logging.error("Something went wrong!")

class Failure():
    def __init__(self, value, failed=False):
        self.value = value
        self.failed = failed
    def get(self):
        return self.value
    def is_failed(self):
        return self.failed
    def __str__(self):
        return ' '.join([str(self.value), str(self.failed)])
    def __or__(self, f):
        if self.failed:
            return self
        try:
            x = f(self.get())
            return Failure(x)
        except:
            return Failure(None, True)

from operator import neg
x = '1'
y = Failure(x) | int | neg | str
print(y)

x = 'hahaha'
y = Failure(x) | int | neg | str
print(y)

class MyClass(object):
    def __init__(self, x):
        self.x = x
    def __del__(self):  #Warning: Perhaps a very bad idea!
        print("I am gone")

my_class = MyClass(1)
del my_class

# my_class

my_class_a = MyClass(1)
my_class_b = my_class_a
my_class_c = MyClass(1)

# Note that this is a reference to the class, therefore, they are pointing to the same thing which is why it changes.
my_class_b.x = 2
print(my_class_a.x)

print(my_class_b == my_class_a)

my_class_a = MyClass(1)
my_class_c = MyClass(1)
print(my_class_a == my_class_c)

from copy import deepcopy
my_class_a = MyClass(1)
my_class_b  =deepcopy(my_class_a)
print(my_class_b == my_class_a)

my_class_b.x = 2
print(my_class_a.x)

# The Ghost Bus Incidence
class GhostBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

#Run this several times
ghost_bus = GhostBus()
ghost_bus.pick("A Ghost")
print(ghost_bus.passengers)
# What goes wrong here? Note that self.passengers is a reference to passengers, and passengers is a refernece to [] (which is global). Note when you mutate self.passengers, you are mutating [] as well. So please use None instead.

a = []
b= [1,a,'2']
b.append(5)
b.extend([1,2])
print(b)

matrix  = [[1,2],[3,4],[5,6],[7,8]]
print(matrix)
tranpose =[[row[i] for row in matrix] for i in range(2)]
print(tranpose)

set_a = {1,2,3}
set_b = {3,4,5}
print(set_a|set_b)
print(set_a - set_b)
print(set_b - set_a)
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a^set_b)

keys = ['a','b','c']
values = [1,2,3]
dict_from_zip = dict(zip(keys, values))
print(dict_from_zip)

# Common Data Structure: NamedTuple
from collections import namedtuple
employee = namedtuple('Employee', ['age', 'place', 'education'])
tom = employee(age=10, place='beijing', education='none')
print(tom)

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class MyDataClass:
    name: str = field(
        default='tom',
        metadata={'help':"Name of the person"}
    )

    age: Optional[int] = field(
        default=None,
        metadata={'help': "Age of the person. Optional."}
    )

    vip: int = field(
        default=100,
        metadata={'help': "Some very important field."}
    )

    def __post_init__(self):    #This function will help you to handle illegal argument.
        if self.vip <= 0:
            raise Exception("That important thing has to be larger than 0")

    @property
    def age_type(self):
        if self.age >= 100:
            return 'You are old'
        else:
            return 'You are still young'

my_data_class = MyDataClass(name='jerry', age=20)
print(my_data_class)
print(my_data_class.age)
print(my_data_class.age_type)

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)
    def __str__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v = Vector(1,2)
print(str(v))
print(v)

v1 = Vector(0, 0)
v2 = Vector(1, 2)
v1 *= 2
print('----------magic-function----------')
print(v1)

# Common Higher Order Function
my_input = [1,2,3,4,5,6,6]
result = map(lambda x: x+1, my_input)
print(result)   #map is lazy
print(list(result))

from functools import reduce
result = reduce(lambda x, y: x+y, filter(lambda x: x > 3, map(lambda x: x+1, my_input)))
print(result)

# Decorators
def my_decorator(func):
    def my_decorator_impl(x):
        result = x if x > 0 else 0
        return func(result)
    return my_decorator_impl

@my_decorator
def myfunc(x):
    return np.sqrt(x)
new_func = my_decorator(myfunc)
print(myfunc(-1))

from functools import partial
def decor_impl(fun, argument):
    def impl(x):
        result = x if x > argument else argument
        print('result: ', result, ' fun(result): ', fun(result))
        return fun(result)
    return impl


decor = partial(decor_impl, argument = 2)


@decor
def myfunc(x):
    return np.sqrt(x)


myfunc(-1)









