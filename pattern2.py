def pypart2(n):
    k = 2*n
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")  
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
pypart2(5)
