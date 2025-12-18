import sys

n,m=map(int,sys.stdin.readline().split())
X=[int(sys.stdin.readline()) for i in range(n)]
Y=[list(map(int,sys.stdin.readline().split())) for i in range(m)]
Z=[]

ANS=0
for y in Y:
    if y[0]==1 and y[1]==10**9:
        ANS+=1
    elif y[0]==1:
        Z.append(y[1])
X.sort(reverse=True)
Z.sort(reverse=True)

XCOUNT=[0]*n#X[i]より大きいZの個数

i=0
j=0
l=len(Z)
X.append(0)
Z.append(0)
while i<l+1 and j<n:
    if Z[i]>=X[j]:
        i+=1
    else:
        XCOUNT[j]=i
        j+=1

count=n
XCOUNT.reverse()
for i in range(n):
    if count>i+XCOUNT[i]:
        count=i+XCOUNT[i]

print(count+ANS)


    
