
def transchar(para_str):
    if type(para_str) == str:
        str_1 = para_str.replace('a', 'h')
        str_2 = str_1.replace('b', 'i')
        return str_2
    else:
        return False

print(type('str'))

print(transchar('abdbi'))

def getvolume(len, width, height):
    return len * width * height

vol = getvolume(2, 12, 13)
print(vol)

def getvolume(len = 0, width = 0, height = 0):
    return len * width * height

vol = getvolume(12, 13)
print(vol)

print("%s, %s, %d" % ("你好", "中国", 2018))


