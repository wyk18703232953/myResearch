d={}
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    d[a]=b
m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    if(a in d and b>d[a]):
        d[a]=b
    elif(a not in d):
        d[a]=b
s=0
for i in d:
    s+=d[i]
print(s)
