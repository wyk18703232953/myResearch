def solve():
    n = int(input())
    l = list(map(int,list(input())))
    divisors = []
    total = sum(l)
    for j in range(2,int(sqrt(total))+1):
        if(total%j==0):
            divisors.extend([j,total//j])
    if(total==0):
        print("YES")
        return
    if(total!=1):
        divisors.append(1)
    # print(divisors)
    for x in divisors:
        search = x
        index = 0
        summ = 0
        while(index<n):
            summ+=l[index]
            if(summ>search):
                break
            elif(summ==search):
                summ = 0
            index+=1
            # print(summ,search)
        if(summ==0 and index==n):
            print("YES")
            return
    print("NO")
import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

solve()



