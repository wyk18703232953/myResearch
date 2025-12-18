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
    n,k=vary(2)
    num=array_int()
    maxi=0.0
    for i in range(n):
        count=1
        sumt=num[i]
        # print(sumt)
        for j in range(i+1,n):
            sumt+=num[j]
            count+=1
            if count>=k:
                # print(sumt,sumt/count)
                maxi=max(maxi,sumt/count)
        # print(maxi)
    if k==1:
        print(max(maxi,max(num)))
    else:
        print(maxi)
    



