import sys
input=sys.stdin.readline
from math import *

l,r=map(int,input().split())
      
l=list(bin(l)[2:])
r=list(bin(r)[2:])
l=['0' for i in range(len(r)-len(l))]+l
#print(l,r)
s=""
for i in range(len(r)):
    if l[i]==r[i]:
        s+="0"
    else:
        s+="1"*(len(r)-i)
        break
print(int(s,2))        