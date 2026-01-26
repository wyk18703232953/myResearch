k=int(input(""))
t=0
if k==0:
    print("Invalid input")
    exit()
d=0
e=0
n=5
while(1):
    u=9*n*(10**n)+1-(10**n)-9*k
    if u>0:
        d+=1
        if e>0:
            u=i
            break
        n=n-1
    elif u<0:
        i=u
        e+=1
        if d>0:
            n=n+1
            break
        n=n+1
    else:
        print(9)
        exit()
import math
u=abs(u)
u=u//9
m=u//n
p=u%(n)
if p==0:
    q=10**(n-1)+m-1
    o=q%10
else:
    q = 10**(n-1) + m
    o=((q//(10**(n-p)))%10)
print(o)