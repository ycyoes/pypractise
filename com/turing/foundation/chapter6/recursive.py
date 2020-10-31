def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

print(factorial(10))

def factorial1(n):
    if n == 1:
        return 1
    else:
        return n * factorial1(n-1)
print(factorial1(10))
print(factorial1(1))

#二分查找
def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) -1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)

print(search(seq, 34))

def func(x):
    return x.isalnum()
seq = ['foo', 'x41', '?!', '***']
print(list(filter(func, seq)))

print(filter(lambda x: x.isalnum(), seq))
filter(lambda x: x.isalnum(), seq)

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
print(reduce(lambda x, y: x + y, numbers))

a = 1, 2
for i in a:
    print(i)
