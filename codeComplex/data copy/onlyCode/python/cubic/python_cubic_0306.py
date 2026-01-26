# @author --> ajaymodi
# optimized approach with memoization (dp)
import sys
# sys.stdin=open("input.in","r")
# sys.stdout=open("output.out","w")

input=lambda : sys.stdin.readline().strip()
char = [chr(i) for i in range(97,123)]
CHAR = [chr(i) for i in range(65,91)]
mp = lambda:list(map(int,input().split()))
INT = lambda:int(input())
rn = lambda:range(INT())


from math import ceil,sqrt,factorial,gcd

r,g,b = mp()
rl = sorted(mp(),reverse=True)
gl = sorted(mp(),reverse=True)
bl = sorted(mp(),reverse=True)



def solve(i,j,k):
	if dp_table[i][j][k] != -1:
		return dp_table[i][j][k]

	ans = 0

	if i < r and j < g:
		ans = max(solve(i+1,j+1,k) + rl[i]*gl[j],ans)

	if i < r and k < b:	
		ans = max(solve(i+1,j,k+1) + rl[i]*bl[k],ans)

	if j < g and k < b:
		ans = max(solve(i,j+1,k+1) + gl[j]*bl[k],ans)

	dp_table[i][j][k] = ans
	return dp_table[i][j][k]
		

dp_table = [[[-1 for i in range(b+1)] for j in range(g+1)] for k in range(r+1)]
res = solve(0,0,0)
print(res)
