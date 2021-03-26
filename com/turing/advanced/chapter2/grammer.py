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

