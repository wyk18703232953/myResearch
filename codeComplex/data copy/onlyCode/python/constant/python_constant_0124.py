n=int(input())
if(n>=0):
    print(n)
else:
    n=abs(n)
    rem=n%10
    n1=n//10
    n2=n1//10
    n2=n2*10+rem
    k=min(n1,n2)
    print(-1*k)
    
    
    
    
    
    
    
