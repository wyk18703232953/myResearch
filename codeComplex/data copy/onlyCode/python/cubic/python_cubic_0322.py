from sys import stdin
input=lambda : stdin.readline().strip()
lin=lambda :list(map(int,input().split()))
iin=lambda :int(input())
main=lambda :map(int,input().split())
from math import ceil,sqrt,factorial,log
from collections import deque
from bisect import bisect_left
def gcd(a,b):
	a,b=max(a,b),min(a,b)
	while a%b!=0:
		a,b=b,a%b
	return b
def solve():
	a,b,c=main()
	x,y,z=lin(),lin(),lin()
	x.sort(reverse=True)
	y.sort(reverse=True)
	z.sort(reverse=True)
	ans=0
	dp=[[[0 for i in range(c+2)] for i in range(b+2)] for i in range(a+1)]
	for i in range(a+1):
		for j in range(b+1):
			for k in range(c+1):
				if i<a and j<b:
					dp[i+1][j+1][k]=max(dp[i+1][j+1][k],dp[i][j][k]+x[i]*y[j])
				if i<a and k<c:
					dp[i+1][j][k+1]=max(dp[i+1][j][k+1],dp[i][j][k]+x[i]*z[k])
				if k<c and j<b:
					dp[i][j+1][k+1]=max(dp[i][j+1][k+1],dp[i][j][k]+z[k]*y[j])
				ans=max(ans,dp[i][j][k])
	print(ans)
qwe=1
# qwe=int(input())
for _ in range(qwe):
	solve()

