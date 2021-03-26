print('-------------chapter2--------')
print(bytes([102,111,111]))

print(list(b'foo bar'))
print(tuple(b'foo bar'))

print(type("some string"))

print(type(b"some bytes"))

print(','.join(['some', 'comma', 'separated', 'values']))

# 1．列表与元组
# 列表推导
print([i for i in range(10) if i % 2 == 0])

# enumerate（枚举）
for i, element in enumerate(['one', 'two', 'three']):
        print(i, element)

# 如果需要一个一个合并多个列表（或任意可迭代对象）中的元素，那么可以使用内置的zip()函数
for item in zip([1,2,3], [4,5,6]):
        print(item)

# 对zip()函数返回的结果再次调用zip()，可以将其恢复原状：
for item in zip(*zip([1,2,3], [4, 5, 6])):
        print(item)

# 序列解包
first, second, third = "foo", "bar", 100
print(first, second, third)

# 带星号的表达式获取单个变量中的多个元素，只要它的解释没有歧义即可。还可以对嵌套序列进行解包
first, second, *rest = 0, 1, 2, 3
print(first, second, rest)

# 带星号的表达式可以获取序列的中间部分
first, *inner, last = 0, 1, 2, 3
print(first, inner, last)

# 嵌套解包
(a, b), (c, d) = (1, 2), (3, 4)
print(a, b, c, d)

# 字典
# 视图对象可以动态查看字典的内容，因此每次字典发生变化时，视图都会相应改变
words = {'foo':'bar', 'fizz':'bazz'}
items = words.items()
words['spam'] = 'eggs'
print(items)

# 在某些情况下，字典的键是连续的，对应的散列值也是连续值（例如整数），那么由于字典的内部实现，元素的顺序可能和添加顺序相同：
print({number: None for number in range(5)}.keys())

# 字典元素的顺序既与对象的散列方法无关，也与元素的添加顺序无关。但我们也不能完全信赖这一说法，因为在不同的Python实现中可能会有所不同。
print({str(number): None for number in range(5)}.keys())
print({str(number): None for number in reversed(range(5))}.keys())

from collections import OrderedDict
dict = OrderedDict((str(number),None) for number in range(5)).keys()
print(dict)


