print(hex(255))

a = [1, 2, 3, 4]
b = a
print(id(a))
print(id(b))

print(a.pop())
print(a)

print(b)

a = [1,2,3,4]
b = a[:]
a.pop()
print(id(a))
print(id(b))

print(a)
print(b)

a = ['a', 'b', 'c', 'd']
for x in a[:]:
    if x == 'c':
        bb = a.pop(0)
    print(x)


for i in range(6):
    if i == 4:
        break
    print(i)

for i in range(6):
    if i == 4:
        continue
    print(i)

for i in range(6):
    print(i)
else:
    print("ok")






