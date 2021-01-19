def fibonacci(xterms):
    n, a, b = 0, 0, 1
    while n < xterms:
        print(b, end = ' ')
        a, b = b, a + b
        n = n + 1
    return 'finished!'

fibonacci(10)

def fibonacci2(xterms):
    n, a, b = 0, 0, 1
    while n < xterms:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'finished!'

fibonacci2(10)
func = fibonacci2(10)
print(func)
print(next(func))
print(next(func))
print(next(func))
for num in func:
    print(num)