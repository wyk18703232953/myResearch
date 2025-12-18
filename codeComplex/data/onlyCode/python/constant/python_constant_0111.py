from collections import Counter
import copy

def solve():
    a,b=list(map(int,input().split()))
    count=0
    if a==b:
        return 1
    while a!=0 and b!=0:
        if a<b:
            count+=(b//a)
            b-=a*(b//a)
        else:
            count+=a//b
            a-=b*(a//b)
    return count


for i in range(int(input())):
        print(solve())

