import sys;input=sys.stdin.readline
# from itertools import accumulate
# from decimal import *
# import math
# getcontext().prec = 50
# s = input().strip()
# n = int(input())
# lis = list(map(int,input().split()))
# x,y = map(int,input().split())
# chars = 'abcdefghijklmnopqrstuvwxyz'

# def gcd(a,b):
#     return gcd (b, a % b) if b else a
        
def solve():
    n, l, r, x = map(int,input().split())
    lis = list(map(int,input().split()))
    lis = sorted(lis)
    dp = [0]
    dp_low = [0]
    dp_high = [0]
    for i in range(len(lis)):
        for j in range(len(dp)):
            if dp_low[j]==0:
                dp_low.append(lis[i])
            else: 
                dp_low.append(dp_low[j])
            dp_high.append(lis[i])
            dp = dp+[dp[j]+lis[i]]
    count = 0
    for i in range(len(dp)):
        if dp[i]>=l and dp[i]<=r and dp_high[i]-dp_low[i]>=x:
            count+=1
    print(count)
    
    
solve()
# for _ in range(int(input())):
#     solve()    