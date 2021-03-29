# 迭代器只不过是一个实现了迭代器协议的容器对象
i = iter('abc')
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

class CountDown:
    def __init__(self, step):
        self.step = step
    def __next__(self):
        """Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        """Return the iterator itself."""
        return self

for element in CountDown(4):
    print(element)


# yield语句
print('-----------yield------------')
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))

print([next(fib) for i in range(10)])


def power(values):
    for value in values:
        print('powering %s' % value)
        yield value
def adder(values):
    for value in values:
        print('adding to %s' % value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

elements = [1, 4, 7, 9, 12, 19]
results = adder(power(elements))
print(next(results))
print(next(results))

def psychologist():
    print('Please tell me your problems')
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much questions")
            elif 'good' in answer:
                print("Ahh that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")


print("------psychologist----------")

free = psychologist()
next(free)

free.send('I feel bad.')
free.send("Why I shouldn't ?")
free.send("ok then i should find what is good for me")

"""
send的作用和next类似，但会将函数定义内部传入的值变成yield的返回值。因此，这个函数可以根据客户端代码来改变自身行为。
为完成这一行为，还添加了另外两个函数：throw和close。它们将向生成器抛出错误。
• throw：允许客户端代码发送要抛出的任何类型的异常。
• close：作用相同，但会引发特定的异常——GeneratorExit。
在这种情况下，生成器函数必须再次引发GeneratorExit或StopIteration。
"""

class WithoutDecorators:
    def some_static_method():
        print("this is static method")
    some_static_method = staticmethod(some_static_method)
    def some_class_method(cls):
        print("this is class method")
    some_class_method = classmethod(some_class_method)

class WithDecorators:
    @staticmethod
    def some_static_method():
        print("this is static method")

    @classmethod
    def some_class_method(cls):
        print("this is class method")

def mydecorator(function):
    def wrapped(*args, **kwargs):
        #在调用原始函数之前，做点什么
        result = function(*args, **kwargs)
        #在函数调用之后，做点什么，并返回结果
        return result
    #返回wrapped作为装饰函数
    return wrapped

class DecoratorAsClass:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        #在调用原始函数之前，做点什么
        result = self.function(*args, **kwargs)
        #在调用函数之后，做点什么，并返回结果
        return result

#参数化装饰器
def repeat(number=3):
    """多次重复执行装饰函数。

    返回最后一次原始函数调用的值作为结果
    :param number: 重复次数，默认值是3
    """

    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator

@repeat(2)
def foo():
    print("foo")

foo()

# 即使参数化装饰器的参数有默认值，但名字后面也必须加括号
@repeat()
def bar():
    print("bar")

bar()






