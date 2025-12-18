from collections import Counter
import string
import math
import sys
# sys.setrecursionlimit(10**6) 
from fractions import Fraction
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(arrber_of_variables):
    if arrber_of_variables==1:
        return int(sys.stdin.readline())
    if arrber_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
testcases=1
for _ in range(testcases):
    n=vary(1)
    indices=array_int()
    cost=array_int()
    ans=float('inf')
    mint=[]
    for i in range(n):
        ans=float('inf')
        total=cost[i]
        flag=0
        for j in range(i):
            if indices[i]>indices[j]:
                ans=min(ans,cost[j])
                flag=1
        if flag!=0:
            total+=ans
            ans=float('inf')
            flag=0
            for k in range(i+1,n):
                if indices[k]>indices[i]:
                    ans=min(ans,cost[k])
                    flag=1
            if flag!=0:
                total+=ans
                mint.append(total)
            else:
                continue
        else:
            continue
    if len(mint)>0:
        print(min(mint))
    else:
        print(-1)


                

                

        