def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num, state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos
    else:
        for pos in range(num):
            if not conflict(state, pos):
               for result in queens(num, state + (pos,)):
                   yield(pos,) + result


print(list(queens(4, (1, 3, 0))))







