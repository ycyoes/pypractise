
#九九乘法表
for i in range(1, 10):
   
    for j in range(1, 10):
        # print(i + "*" + j + "=" + i * j)
        print(i,"*", j , "=", i * j, end="")
        print("\t", end="")
        # print(i, j)
    print()