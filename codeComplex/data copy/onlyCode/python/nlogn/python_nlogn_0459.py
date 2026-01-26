import math
import copy
def dtb(n): 
    return bin(n).replace("0b","")
def btd(n): 
    return int(n,2) 
t=1
for k in range(t):
    n,kk=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    c=copy.copy(a)
    a.sort(reverse=True)
    b=[]
    f=[]
    ans=0
    for i in range(kk):
        ans+=a[i]
        b.append(a[i])
    count=1    
    x=0
    y=0
    for i in range(n):
        if len(f)==(kk-1):
            y=i
            break
        if c[i] in b:
            f.append(i-x+1)
            x=i+1
            b.remove(c[i])
            
    f.append(n-y)        
    print(ans)    
    for i in f:
        print(i,end=" ")
        