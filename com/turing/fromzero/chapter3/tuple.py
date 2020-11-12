print(1,2,3)

#包含一个值的元组的实现方式有一些奇特，必须在括号中的元素后加一个逗号
print((1,))

mix = ('hello', 'world', 2015, 2016)
print("mix[1] is: ", mix[1])

field = ('hello', 'world')
num = (2015, 2016)
print(field + num)

# del field 
print(field)

#tuple(seq)用于将列表转换为元组。使用方式如下：
field = ['hello', 'world', 'welcome']
tup = tuple(field)
print(tup)

#tuple -------------> list
tup = (123, 'hello', [23, '中国'], ('python3.7', 'learn'))
print(tup)

tup2ls = list(tup)
print(tup2ls)

# list ---------------> tuple
ls2tup = tuple(tup2ls)
print(ls2tup)