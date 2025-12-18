from sys import stdin,stdout,setrecursionlimit
stdin.readline
def mp(): return list(map(int, stdin.readline().strip().split()))
def it():return int(stdin.readline().strip())
from collections import defaultdict as dd,Counter as C,deque
from math import ceil,gcd,sqrt,factorial,log2,floor	
from bisect import bisect_right as br,bisect_left as bl
from heapq import *
mod = 10**9+7


def solve():
	n = it()
	v=[0]*(n+1)
	for i in range(1,n+1):
		v[i] = input()
	
	dp=[[0]*(n+2) for _ in range(n+1)]

	for l in range(n+2):
		dp[n][l] = 1

	for i in range(n-1,0,-1):
		curr_sum = 0
		for l in range(n):
			curr_sum += dp[i+1][l]
			curr_sum%=mod
			if v[i] == 'f':
				dp[i][l] = dp[i+1][l+1]
			else:
				dp[i][l]= curr_sum

	print(dp[1][0])

solve()
