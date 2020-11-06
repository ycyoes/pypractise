def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queens(num=8, state=()):
        for pos in range(num):
            if not conflict(state, pos):
                if len(state) == num-1:
                 yield (pos,)
            else:
               for result in queens(num, state+(pos,)):
                   yield (pos,)+result
#(pos,)中的逗号必不可少（不能仅用圆括号将pos括起），这样得到的才是元组。

print(list(queens(3)))
print(list(queens(4)))

for solution in queens(8):
    print(solution)


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. '*(pos) + 'X' + '. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

import random
prettyprint(random.choice(list(queens(8))))


