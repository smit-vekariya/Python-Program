def recu_sum(n):
    if n<1:
        return 0
    else:
        return n+recu_sum(n-1)
        


sumn=10
print(recu_sum(sumn))