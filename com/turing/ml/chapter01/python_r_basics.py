
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











