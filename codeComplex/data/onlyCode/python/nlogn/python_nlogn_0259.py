import sys
input=sys.stdin.readline
n=int(input())
c=[]
for _ in range(n):
    a,b=map(int,input().split())
    c.append((a,b,_))
c.sort(key=lambda x:(x[0],-x[1]))
a=c[0][1]
b=c[0][2]
an1=-1
an2=-1
for i in range(1,n):
    if c[i][1]<=a:
        an2=b+1
        an1=c[i][2]+1
        break
    else:
        a=c[i][1]
        b=c[i][2]
print(an1,an2)