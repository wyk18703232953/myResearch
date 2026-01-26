from collections import defaultdict as dd
import math
import sys
import heapq
import copy
input=sys.stdin.readline
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return map(int, input().split())

def lm():
	return list(map(int, input().split()))


def solve():

	r,g,b = mi()

	rs = lm()
	gs = lm()
	bs = lm()
	rs.sort()
	gs.sort()
	bs.sort()

	ans = [[[0 for i in range(b+1)] for i in range(g+1)] for i in range(r+1)]

	for i in range(1,r+1):
		for j in range(1,g+1):
			ans[i][j][0]= ans[i-1][j-1][0]+rs[i-1]*gs[j-1]


	for i in range(r+1):
		for j in range(g+1):
			for k in range(1,b+1):
				new_len = bs[k-1]
				if i==0:
					i_len = 0
				else:
					i_len = ans[i-1][j][k-1] + rs[i-1]*new_len
				if j==0:
					j_len = 0
				else:
					j_len = ans[i][j-1][k-1] + gs[j-1]*new_len
				if i>0 and j>0:
					i_j_len = ans[i-1][j-1][k]+rs[i-1]*gs[j-1]
				else:
					i_j_len = 0
				ans[i][j][k] = max(i_len,
									j_len,
									ans[i][j][k-1],
									i_j_len)
	#print(ans)
	print(ans[r][g][b])





solve()
