import sys
import math
import collections
import bisect
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
for t in range(1):
    n=int(input())
    arr=get_list()
    counter=collections.Counter(arr)
    ans=set()
    for i in counter:
        for j in range(1,32):
            no=2**j
            diff=no-i
            if diff<0:
                continue
            if diff==i:
                if counter[i]>1:
                    ans.add(i)
                    #print(i,no,diff,"###")
                    break
            else:
                if diff not in  counter:
                    continue
                else:
                    ans.add(i)
                    #print(i,no,diff)
                    break
    #print(ans)
    val=0
    ans=list(ans)
    for i in ans:
        val+=counter[i]
    print(n-val)