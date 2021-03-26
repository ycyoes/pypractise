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