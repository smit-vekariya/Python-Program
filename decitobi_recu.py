def dtob_recu(n):
    if n>1:
        dtob_recu(n//2)
    print(n%2,end="")

num=2
dtob_recu(num)
print()