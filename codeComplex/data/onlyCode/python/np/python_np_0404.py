import sys
input = sys.stdin.readline

n,m=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]

SET=set()
for a in A:
    SET|=set(a)

compression_dict={a: ind for ind, a in enumerate(sorted(SET))}

for i in range(n):
    A[i]=[compression_dict[a] for a in A[i]]

OK=0
NG=len(compression_dict)
ANS=[1,1]
B=[set()]*n
P=[2,3,5,7,11,13,17,19]
Q=1
for j in range(m):
    Q*=P[j]
    
import math

def ya(x):
    xr=math.ceil(math.sqrt(x))

    LIST=[]
    for i in range(1,xr+1):
        if x%i==0:
            LIST.append(i)
            LIST.append(x//i)

    return LIST

while NG>OK+1:
    mid=(OK+NG)//2
    SET=set()

    for i in range(n):
        NOW=1
        for j in range(m):
            if A[i][j]>=mid:
                NOW*=P[j]
        B[i]=NOW
        SET.add(NOW)

    #print(mid,SET)
    flag=0

    for s in SET:
        for l in ya(s):
            if Q//l in SET:
                flag=1
                OK=mid
                break
        if flag:
            break

    else:
        NG=mid

SET=set()
for i in range(n):
    NOW=1
    for j in range(m):
        if A[i][j]>=OK:
            NOW*=P[j]
    B[i]=NOW
    SET.add(NOW)

flag=0
for i in range(n):
    for l in ya(B[i]):
        if Q//l in SET:
            ANS1=i
            flag=1
            break
    if flag:
        break

LIST=ya(B[i])
SET=set(LIST)

for i in range(n):
    if Q//B[i] in SET:
        ANS2=i

print(ANS1+1,ANS2+1)
