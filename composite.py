def com(p):
    c=0
    n=1
    while c<p:
        n=n+1
        for i in range(2,n-1):
            if(n%i)==0:
                c=c+1
                if(c==p):
                  print(n)
                break
    
  
        
com(10)