import sys
input=sys.stdin.readline
hashi=dict()
for i in range(1,10**5):
    hashi[i*i]=1
    hashi[(2*i*i)]=1
t=int(input())
for you in range(t):
    n=int(input())
    if(n%2):
        print("NO")
        continue
    z=n//2
    if(z in hashi):
        print("YES")
    else:
        print("NO")
