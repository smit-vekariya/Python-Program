x=[[3,2,3],
    [4,5,6],
    [7,8,9]]
y=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        y[i][j]=x[i][j]
for r in y:
    print(r)