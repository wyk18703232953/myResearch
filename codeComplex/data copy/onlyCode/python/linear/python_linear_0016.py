def f(n):
    k=2
    while k*k<=n:
        if n%k==0:
            return False
        k+=1
    return True
n,k=map(int,input().split())
a=[]
x=0
for i in range(2,n+1):
    if f(i):
        a.append(i)
for i in range(len(a)-2):
    if a[i]+a[i+1]+1 in a:
        x+=1
if x>=k:
    print('YES')
else:
    print('NO')
