fhand = open('d:/python.txt', 'r')
print(fhand)

for line in fhand:
    print(line)

fhand.seek(0)
# print(fhand.read())

print('-------readline-------')
print(fhand.readline())