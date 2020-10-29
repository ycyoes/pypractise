for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

#求平方
squares = []
for val in range(1, 11):
    square = val ** 2
    squares.append(square)
print(squares)

sqs = [val ** 2 for val in range(1, 11)]
print(sqs)

#元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)








