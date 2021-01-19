
#character of line change
a = 15
if a >= 10:
    print("a is larger than 10!")
else:
    print("a is smaller than 10")

print("good good study, \
      day day up!")


dir = dir(__builtins__)
print(dir)

print("--------tuple--------")
val = 1,2,3,4
print(type(val))
print(val)

a,b,c,d=val
print(a,b,c,d)
print(type(a))

n = 10
b = (x**2 for x in range(n) if x % 2 ==0)
print(b)
print(type(b))

print(next(b))
print(next(b))
print(next(b))
print(b.__next__())

c = (x**2 for x in range(n) if x % 2 ==0)
#Iterate b through Python Syntactic Sugar
for num in c:
    print(num)





