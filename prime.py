def prime(l,h):
  for n in range(l,h):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                print(f"{n} not")
                break        
        else:
            print(f"{n} prime")
    else:
        print(f"{n} not")
        
num=prime(2,10)