#: Author - Soumya Saurav
import sys,io,os,time
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect,math,heapq
alphabet = "abcdefghijklmnopqrstuvwxyz"

input = sys.stdin.readline

########################################
'''
3 3 3 
1 2 3
1 2 3
1 2 3

'''
'''
nax = 201

nr , ng , nb = map(int, input().split())
n = nr + ng + nb
r = list(map(int , input().split()))
g = list(map(int , input().split()))
b = list(map(int , input().split()))

r.sort()
g.sort()
b.sort()

dp = [[[0]*nax for i in range(nax)] for j in range(nax)]
'''
'''
arr = [[1,i] for i in r] + [[2,i] for i in b] + [[3,i] for i in g]
arr.sort(key = lambda x : x[1],reverse = True)
ans = 0
done = [False]*n
print(arr)
for i in range(n):
	ok = False
	if done[i]: continue
	for j in range(i+1,n):
		if done[j]: continue
		if arr[i][0] != arr[j][0]:
			print(i+1,j+1,arr[i][1]*arr[j][1])
			ans += arr[i][1]*arr[j][1]
			done[i] = True
			done[j] = True
			ok = True
			break
	if not ok: break
print(ans)

'''
'''
sys.setrecursionlimit(10**7)


from functools import lru_cache
@lru_cache(None)
def f(i,j,k):
	#print(i,j,k)
	if (i >= nr and j >= ng) or (j >= ng and k >= nb) or (i >= nr and k >= nb):
		return 0
	ans = r[i]*g[j] + f(i+1,j+1,k) if i < nr and j < ng else 0
	#print(ans)
	if i < nr and k < nb:
		ans = max(ans , r[i]*b[k] + f(i+1,j,k+1)) 
	#print("???:",ans,r[k]*r[j] + f(i,j+1,k+1))
	if k < nb and j < ng:
		ans = max(ans, g[j]*b[k] + f(i,j+1,k+1))
	#print(ans)
	return ans
print(f(0,0,0))
	
'''
def solve():
  r, g, b = map(int, input().split());R,G,B = sorted(list(map(int, input().split()))),sorted(list(map(int, input().split()))),sorted(list(map(int, input().split())));dp = [[[0]*(b+1) for _ in range(g+1)] for _ in range(r+1)]
  for i in range(r+1):
    for j in range(g+1):
      for k in range(b+1):
        if i+j+k<2:continue
        if i>0 and j>0:dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-1][k]+R[i-1]*G[j-1])
        if i>0 and k>0:dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k-1]+R[i-1]*B[k-1])
        if j>0 and k>0:dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k-1]+G[j-1]*B[k-1])
  return dp[r][g][b]
print(solve())



