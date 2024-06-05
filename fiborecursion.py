def recu_fibo(n):
    if n<=1:
        return n
    else:
        return(recu_fibo(n-1)+recu_fibo(n-2))
nt=10
if nt<=0:
    print("Plase enter valid number")
else:
    for i in range(nt):
        print(recu_fibo(i))