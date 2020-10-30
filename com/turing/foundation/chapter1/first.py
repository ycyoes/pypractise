#使用repr时，通常会获得值的合法Python表达式表示。
print(repr('Hello,\nWorld!'))

'''test'''
print('''This is a very long string. It continues here.
And it's not over yet. "Hello, world!"
Still here.''')

# print(r"This is illegal\")

print(r'C:\Program Files\foo\bar' '\\')

print('hello, world!'.encode('ASCII'))
print('hello, world!'.encode('UTF-8'))
print('hello, world!'.encode('UTF-32'))

x = bytearray(b"hello")
x[1] = ord(b'u')
print(x)