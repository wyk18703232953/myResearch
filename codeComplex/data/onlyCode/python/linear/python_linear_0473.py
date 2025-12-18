import sys
import io, os
import math
from heapq import *
gcd = math.gcd
sqrt = math.sqrt
ceil = math.ceil
# arr=list(map(int, input().split()))
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def strinp(testcases):
    k = 5
    if (testcases == -1 or testcases == 1):
        k = 1
    f = str(input())
    f = f[2:len(f) - k]
    return f
def ind(ch):
    return ord(ch)-ord("a")
def main():
    n=int(input())
    b=[0]
    cost=b+list(map(int, input().split()))
    arr=b+list(map(int, input().split()))
    nv=[-1]*(n+1)
    colors=[]
    c=0
    for i in range(1,n+1):
        if(nv[i]!=-1):
            continue
        nv[i]=c
        dest=arr[i]
        while(nv[dest]==-1):
            nv[dest]=c
            dest=arr[dest]
        if(nv[dest]==c):
            colors.append(dest)
        c+=1
    s=0
    for i in colors:
        mi=cost[i]
        nxt=arr[i]
        while(nxt!=i):
            mi=min(mi,cost[nxt])
            nxt=arr[nxt]
        s+=mi
    print(s)
main()