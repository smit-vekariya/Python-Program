def fc(num):
    
    if num==1:
        return num
    else:
        return num*fc(num-1)


num=5
print(fc(num))