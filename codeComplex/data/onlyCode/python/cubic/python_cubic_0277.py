import sys
import math
from math import *
from collections import Counter,defaultdict
from io import BytesIO, IOBase
from collections import deque


def rec(i,j,k):
	if (i == rl and j == bl) or (i == rl and k == gl) or (k == gl and j == bl):
		return 0
	if dp[i][j][k] != -1:
		return dp[i][j][k]
	else:
		x = r[i]*b[j]
		y = b[j]*g[k]
		z = r[i] * g[k]
		if x>0:
			x += rec(i+1,j+1,k)
		if y>0:
			y += rec(i,j+1,k+1)
		if z>0:
			z += rec(i+1,j,k+1)

		dp[i][j][k] = max(x,y,z)
		return dp[i][j][k]

def main():
	global r,g,b,rl,bl,gl,dp

	rl,bl,gl = list(map(int, input().split()))
	r = list(map(int, input().split())) + [0]
	b = list(map(int, input().split())) + [0]
	g = list(map(int, input().split())) + [0]
	cnt =3
	i =j = k = 0
	ans = 0
	dp=[[[-1 for i in range(gl+1)] for j in range(bl+1)]for k in range(rl+1)] 
	r.sort(reverse = True)
	b.sort(reverse = True)
	g.sort(reverse = True)

	print(rec(i,j,k))
	


main()