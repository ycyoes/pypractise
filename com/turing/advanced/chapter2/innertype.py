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






