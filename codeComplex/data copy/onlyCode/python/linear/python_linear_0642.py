import sys

n=int(input())
A=list(map(int,input().split()))

#import random
#A=[random.randint(1,3) for i in range(10)]
#n=len(A)
#A=[2, 1, 1, 1, 3, 1, 2, 3, 1, 3]
#n=10

if sum(A)<2*n-2:
    print("NO")
    sys.exit()

ONES=A.count(1)
print("YES",min(n-1,n-ONES+1))

NOONE=[]
for i in range(n):
    if A[i]!=1:
        NOONE.append([A[i],i+1])

#print(NOONE)
ANS=[]
for i in range(1,len(NOONE)):
    ANS.append((NOONE[i-1][1],NOONE[i][1]))
    NOONE[i-1][0]-=1
    NOONE[i][0]-=1

#print(NOONE,ANS)

NOONE=[[1,NOONE[-1][1]]]+NOONE[0:-1]+[[NOONE[-1][0]-1,NOONE[-1][1]]]

#print(NOONE)
LENNO=len(NOONE)

j=0
for i in range(n):
    while j<LENNO and NOONE[j][0]==0:
        j+=1
    if A[i]!=1:
        continue
    ANS.append((i+1,NOONE[j][1]))
    NOONE[j][0]-=1


print(len(ANS))
for a,b in ANS:
    print(a,b)
    
        
