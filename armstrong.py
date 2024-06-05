"""num=152
lnum=len(str(num))
sum=0
cnum=num
while(num>0):
    d=num%10
    sum+=d**lnum
    num=num//10
if(sum==cnum):
    print(f"yes, {cnum} is Armstrng number.")
else:
    print(f"No, {cnum} is not Armstrng number.")
"""
def arm(l,u):
    for num in range(l,u):
        snum=str(num) 
        sum=0
        lnum=len(snum)  
        for i in snum:   
            sum+=int(i)**lnum
        if sum==num:
            print(f"{sum} armstrong")
    
arm(2,500)

    