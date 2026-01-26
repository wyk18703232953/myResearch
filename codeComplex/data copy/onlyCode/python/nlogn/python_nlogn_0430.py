import bisect
from collections import defaultdict,Counter
import math

    
def solve(a):
    count=0
    mp=Counter(a)
    for i in range(len(a)):
        flag=0
        for j in range(31):
            x=int(1<<j)-a[i]
            if (x in mp) and (x==a[i] and mp[x]>1):
                # print(x)
                flag=1
                break
            elif (x in mp) and (x!=a[i] and mp[x]>0):
                flag=1
                break
        if flag==0:
            count+=1        

    return count


n=int(input(''))
a=list(map(int,input('').split()))
print(solve(a))
