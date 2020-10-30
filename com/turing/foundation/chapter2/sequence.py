
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
    + ['st', 'nd', 'rd'] + 7 * ['th'] \
    + ['st']

print(endings)

#序列相加
print([1,2,3] + [3, 4,5,6])

print([42] * 10)

database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]

username = input('User name: ' )
pin = input('PIN code: ')
if [username, pin] in database:
    print('Access granted')

    