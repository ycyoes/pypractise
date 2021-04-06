
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

def printf(format, *arg):
    print(format%arg)

printf("年后")

printf("%s,%s", "你好", "中国")
printf("%s, %s, %d" % ("你好", "中国", 2018))

def getchange(*arg):
    print(arg)

getchange(1,2,3)

def addall(*arg):
    total = 0
    for arg_one in arg:
        total += arg_one
    return total

aa = addall(1,2,3,4)
print(aa)

# *arg、**argv只能够放到参数的最后，并且*arg必须放到**argv之前，可变参数只能放到固定参数后面
def funexe(keyparam, choice=1, *arg, **keywords):
    print(keyparam, choice,arg,keywords)

funexe('a', 'b', 'c', 'e')
funexe('a', 'b', 'c', 'e', three=3)

def addtwo(a, b):
    return a + b
addtwo(1,2)

add1=addtwo
add1(3,5)

def test2(fun, a, b):
    return fun(a,b)

test2(add1,3,4)

def addtwo(a,b):
    a + b

# 对一个函数，需要有返回值时，可以使用return语句。若不使用return语句，则返回为None类型
print(addtwo(2,3))

class Student():
    def __init__(self, score1, score2, score3):
        self.scores = [score1, score2, score3]

stu_1 = Student(80, 90, 85)
print(stu_1.scores)

# lambda函数
b = lambda a, b:a+b
c = b(1,2)
print(c)

g = lambda x, y=0, z=0: x+y+z
d = g(4,5,6)
print(d)

def isPrime(n):
    mid = int(pow(n,0.5)+1)
    for i in range(2,mid):
        if n % i == 0: return False
    return True

primes=[]

for i in range(2,100):
    if isPrime(i): primes += [i]

print(primes)

mid = int(pow(1,0.5)+1)
print('mid: %s' % mid)

from functools import reduce
print(reduce(lambda l,y: not 0 in map(lambda x:y % x, l) and l+[y] or l, range(2, 100), []))

# 嵌套函数
def getfun(x,y):
    def addfun(a,b):
        return a*b
    return addfun(x,y)

print(getfun(2,3))

# 函数作用域
var = []
def test2():
    var=[1]
    var.append(1)
    return var

print(test2())

print(var)

def test3():
    var.append(2)
    return var

print(test3())

#八皇后问题
# （1）象棋棋盘的数据结构
chess = [[0 for x in range(8)] for x in range(8)]
print(chess)
# （2）安全位置的判断根据象棋棋盘数据结构的设计，凡是元素值为0的都是安全的，凡是元素值不为0的都是不安全的。
# 可以使用下面的函数来实现这个功能：

def judgedanger(chess,x,y):
    if chess[x][y] == 0:
        return True
    else:
        return False

# （3）回溯功能的实现
def setdanger(chess,x,y):
    for col in range(len(chess)):
        for row in range(len(chess[0])):
            if col == x:
                chess[col][row] +=1
            elif row == y:
                chess[col][row] +=1
            elif col + row == x + y:
                chess[col][row] += 1
            elif col - row == x - y:
                chess[col][row] += 1
            else:
                pass

def erasedanger(chess,x,y):
    for col in range(len(chess)):
        for row in range(len(chess[0])):
            if col == x:
                chess[col][row] -= 1
            elif row == y:
                chess[col][row] -= 1
            elif col + row == x + y:
                chess[col][row] -= 1
            elif col - row == x - y:
                chess[col][row] -= 1
            else:
                pass

def judgecol(chess,col):
    for row in range(len(chess[col])):
        if judgedanger(chess,col,row):
            break
    else:
        return False
    return True

def tryqueen(chess,col,flag,result):
    flag[0]=True
    if col==8:
        print("find")
    else:
        if judgecol(chess,col):
            for row in range(len(chess[col])):
                if judgedanger(chess,col,row):
                    print("ok"+str(col)+":"+str(row))
                    setdanger(chess,col,row)
                    result.append((col,row))
                    tryqueen(chess,col+1,flag,result)
                    if flag[0]==False:
                        erasedanger(chess,col,row)
                        result.pop()
                else:
                    flag[0]=False


# reduce
scientists = ({'name':'Alan Turing', 'age': 105, 'gender':'male'},
              {'name':'Dennis Ritchie', 'age': 76, 'gender':'male'},
              {'name':'Ada Lovelace', 'age': 202, 'gender':'female'},
              {'name':'Frances E. Allen', 'age': 84, 'gender':'female'})


def reducer(accumulator, value):
    print('accumulator: ', accumulator, ' value: ', value)
    sum = accumulator + value['age']
    return sum


total_age = reduce(reducer, scientists, 0)
print(total_age)






