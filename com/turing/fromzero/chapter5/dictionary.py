student = {'小萌': '1001', '小智': '1002', '小强': '1005', '小张': '1006'}
print(type(student))

seq = ('name', 'age', 'sex')
info = dict.fromkeys(seq)
print(info)

info = dict.fromkeys(seq, 10)
print(info)

print(info.items())

#setdefault()方法和get()方法类似，用于获得与给定键相关联的值。如果键不存在于字典中，就会添加键并将值设为默认值。
print("key: %s" % info.setdefault('name'))

a = dict()
print(a)