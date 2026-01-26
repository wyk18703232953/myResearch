import sys
from math import sqrt, gcd, ceil, log, floor
from bisect import bisect, bisect_left
from collections import defaultdict, Counter, deque
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
read = lambda: list(map(int, input().strip().split()))

MOD = 10**9 + 7


def main():
	# ans_ = []
	# ans_.append(ans)
	# print(("\n").join(map(str, ans_)))
	r, g, b = read()
	r_ar=sorted(read(), reverse = True); g_ar = sorted(read(), reverse = True); b_ar = sorted(read(), reverse = True)
	N = 201
	dp = [[[-1]*N for i in range(N)]for j in range(N)]
	# for i in dp:print(*i)
	def f(x, y, z):
		# print(x, y, z, (x >= r) + (y >= g) + (z >= b))
		if ((x >= r) + (y >= g) + (z >= b)) >= 2:
			return(0)
		if dp[x][y][z] != -1:
			return(dp[x][y][z])
		maxi = 0
		if x < r and y < g:
			maxi = max(maxi, r_ar[x]*g_ar[y] + f(x+1, y+1, z))
		if z < b and y < g:
			maxi = max(maxi, b_ar[z]*g_ar[y] + f(x, y+1, z+1))
		if x < r and z < b:
			maxi = max(maxi, r_ar[x]*b_ar[z] + f(x+1, y, z+1))
		dp[x][y][z] = maxi
		return(maxi)
	print(f(0, 0, 0))





if __name__ == "__main__":
	main()