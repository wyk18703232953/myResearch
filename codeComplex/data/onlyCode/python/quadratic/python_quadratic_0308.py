import sys
import math
import collections
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
for t in range(1):
    n,k=get_ints()
    arr=get_list()
    ans=0
    for i in range(n):
        val=arr[i]
        c=1
        sol=0
        if c >= k:
            sol = max(sol, val / c)
        for j in range(i+1,n):
            val+=arr[j]
            c+=1
            if c>=k:
                sol=max(sol,val/c)
        ans=max(sol,ans)
    print(ans)