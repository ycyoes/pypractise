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


