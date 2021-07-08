from functools import reduce

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list element is: ", end="")
print(reduce(lambda a, b:a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is: ", end="")
print(reduce(lambda a, b: a if a>b else b, lis))

my_input = [1,2,3,4,5,6,6]
result = map(lambda x: x+1, my_input)
print(result)
print(list(result))

result = reduce(lambda x, y: x+y, filter(lambda x: x>3, map(lambda x: x+1, my_input)))
print(result)