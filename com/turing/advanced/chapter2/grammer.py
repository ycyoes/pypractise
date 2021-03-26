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








