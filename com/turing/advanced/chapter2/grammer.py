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

def dummy_decorator(function):
    def wrapped(*args, **kwargs):
        """包装函数内部文档。"""
        return function(*args, **kwargs)
    return wrapped

@dummy_decorator
def function_with_important_docstring():
    """这是我们想要保存的重要文档字符串。"""

print(function_with_important_docstring.__name__)
print(function_with_important_docstring.__doc__)

from functools import wraps

def preserving_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        """包装函数内部文档。"""
        return function(*args, **kwargs)
    return wrapped

@preserving_decorator
def function_with_important_docstring():
    """这是我们想要保存的重要文档字符串。"""


print(function_with_important_docstring.__name__)
print(function_with_important_docstring.__doc__)

rpc_info = {}

def xmlrpc(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        #注册签名
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)
        def _check_types(elements, types):
            """用来检查类型的子函数。"""
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError(
                    'arg #%d should be %s' % (index, of_the_right_type)
                )
        #包装过的函数
        def __xmlrpc(*args): #没有允许的关键词
            #检查输入的内容
            checkable_args = args[1:] #去掉self
            _check_types(checkable_args, in_)
            #运行函数
            res = function(*args)
            #检查输出的内容
            if not type(res) in (tuple, list):
                checkable_res = (res, )
            else:
                checkable_res = res

            _check_types(checkable_res, out)
            #函数及其类型检查成功
            return res
        return __xmlrpc
    return _xmlrpc
# 装饰器将函数注册到全局字典中，并将其参数和返回值保存在一个类型列表中

class RPCView:
    @xmlrpc((int, int)) # two int -> None
    def meth1(self, int1, int2):
        print('received %d and %d' % (int1, int2))

    @xmlrpc((str, ), (int, )) #string -> int
    def meth2(self, phrase):
        print('received %s' % phrase)
        return 12
# 在实际读取时，这个类定义会填充rpc_infos字典，并用于检查参数类型的特定环境中
print(rpc_info)

my = RPCView()
my.meth1(1,2)


# 缓存
import time
import hashlib
import pickle

cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(function):
        # print('----------function-----------\n', function)
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            # 是否已经拥有它了？
            if(key in cache and not is_obsolete(cache[key], duration)):
                print('we got a winner')
                return cache[key]['value']
            # 计算
                result = function(*args, **kw)
                # 保存结果
                cache[key] = {
                    'value': result,
                    'time': time.time()
                }
                return result
            return __memoize
        return _memoize

@memoize
def very_very_very_complex_stuff(a, b):
    return a + b


very_very_very_complex_stuff(2, 2)

















