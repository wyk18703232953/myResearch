import sys
import math
import collections
import heapq
input=sys.stdin.readline
k1,k2,k3=(int(i) for i in input().split())
l=[k1,k2,k3]
if(1 in l):
    print("YES")
elif(l.count(2)>=2):
    print("YES")
elif(l.count(3)==3):
    print("YES")
elif(sorted(l)==[2,4,4]):
    print("YES")
else:
    print("NO")