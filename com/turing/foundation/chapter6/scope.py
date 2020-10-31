x = 1
scope = vars()
print(scope['x'])

def combine(parameter):
    print(parameter + globals()['parameter'])

parameter = 'berry'
combine('Shrub')

#像multiplyByFactor这样存储其所在作用域的函数称为闭包。
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor

double = multiplier(2)
print(double(5))





