bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print("最后一个元素: " + bicycles[-1])

#修改数组元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#添加元素
motorcycles.append('test')
print(motorcycles)

#插入元素
motorcycles.insert(0, 'insert')
print(motorcycles)

#删除元素
del motorcycles[0]
print(motorcycles)

#字母顺序相反的顺序排列
motorcycles.sort(reverse=True)
print(motorcycles)

print('length: ', len(motorcycles))
