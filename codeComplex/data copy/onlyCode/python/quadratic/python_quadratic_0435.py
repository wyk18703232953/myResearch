import math
#n,s = map(int, input().strip().split(' '))
n=int(input())
#lst = list(map(int, input().strip().split(' ')))
s2=input()
s2=list(s2)
s=[]
for i in range(n):
    if s2[i]=='0':
        continue
    else:
        s.append(int(s2[i]))
s1=sum(s)
n=len(s)
l=[]
for i in range(2,n+1):
    if s1%i==0:
        l.append(s1//i)
f=0
if len(s)==0:
    f=1
for i in range(len(l)):
    c=0
    if f==1:
        break
    for j in range(n):
        c+=s[j]
        if c==l[i]:
            c=0
            if j==n-1:
                f=1
        elif c<l[i]:
            c=c
        else:
            break
if f==0:
    print('NO')
else:
    print('YES')