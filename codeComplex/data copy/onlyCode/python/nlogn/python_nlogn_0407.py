import sys
input=sys.stdin.buffer.readline
from collections import defaultdict as dd
n=int(input())
d=dd(int)
for i in range(n):
    l,r=map(int,input().split())
    d[l] +=1
    d[r+1] -=1
arr=list(d.keys())
arr.sort()
ans=[0 for i in range(n+1)]
count =0
l=len(arr)
arr.append(arr[-1])
for i in range(l):
    count +=d[arr[i]]
    ans[count] +=arr[i+1] -arr[i]
print(*ans[1:])