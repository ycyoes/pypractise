
#字符串的find方法返回的不是布尔值。如果返回0，就表示在索引0处找到了子字符串。
field = 'do it now'
print(field.find('do'))
print(field.find('now'))
print(field.find('python'))

dirs = '', 'home', 'data', 'hdfs'
print('path: ', '/'.join(dirs))

'''
str.translate(table[, deletechars])
此语法中，str代表指定检索的字符串；
table代表翻译表，翻译表通过maketrans方法转换而来；
deletechars代表字符串中要过滤的字符列表。返回结果为翻译后的字符串。
'''
intab = 'adefs'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
st = 'just do it'
print(st.translate(trantab))