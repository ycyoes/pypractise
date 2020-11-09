'''
要检查对象是否类似于字符串，最简单、最快捷的方式是，尝试将对象与一个字符串拼接起来，
并检查这是否会引发TypeError异常
'''

def flatten(netsted):
    try: 
        #不迭代类似于字符串的对象
        try: netsted + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in netsted:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield netsted

print(list(flatten(['foo', ['bar', ['baz']]])))

'''
请注意，这里没有执行类型检查：我没有检查nested是否是字符串，而只是检查其行为是否类似于字符串，
即能否与字符串拼接。对于这种检查，一种更自然的替代方案是，
使用isinstance以及字符串和类似于字符串的对象的一些抽象超类，但遗憾的是没有这样的标准类。
另外，即便是对UserString来说，也无法检查其类型是否为str。
'''

print(list(flatten([1, 2])))
