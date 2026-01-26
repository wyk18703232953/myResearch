#n=int(input())
n,m=map(int,input().split())

vert=[]

for i in range(n):
    v=int(input())
    vert.append(v)

horz=[]

for i in range(m):
    x1,x2,y=map(int,input().split())
    if x1==1:
        horz.append(x2)

vert.sort()
horz.sort()

vert.append(1000000000)

def next(k,a,x):
    while k<len(a) and a[k]<x:
        k+=1
    return k

num=next(0,horz,vert[0])

ans=len(horz)-num

for i in range(1,len(vert)):
    num2=next(num,horz,vert[i])
    t=i+len(horz)-num2
    if t<ans: ans=t
    num=num2

print(ans)




