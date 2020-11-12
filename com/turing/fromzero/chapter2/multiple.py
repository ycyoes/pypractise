
#九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # print(i + "*" + j + "=" + i * j)
        # print(i,"*", j , "=", i * j, end="")
        # print("\t", end="")
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
        # print(i, j)
    print()