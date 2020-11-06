def flatten(nested):
    result = []
    try: 
        #不迭代类似于字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result


nested = [[1, 2], [3, 4], [5]]

for num in flatten(nested):
    print(num)

print(list(flatten(nested)))








