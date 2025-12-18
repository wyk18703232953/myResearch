import sys
import math

n=int(input())
lista=[int(x) for x in input().strip().split()]
pap=lista[:]
pap.sort()
if(pap[-1]==1):
    pap[-1]=2
else:
    pap=[1]+pap[:-1]
for i in range(n):
    print(pap[i], end=" ")
