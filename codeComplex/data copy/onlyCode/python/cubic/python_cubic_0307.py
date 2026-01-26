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
 
	if i < r and j < g and k < b:
		m = max(solve(i+1,j+1,k)+(rl[i]*gl[j]), solve(i+1,j,k+1)+(rl[i]*bl[k]), solve(i,j+1,k+1)+(gl[j]*bl[k]))
		dp_table[i][j][k] = m
		return m
 
	elif i < r and j < g:
		m = solve(i+1,j+1,b) + rl[i]*gl[j]
		dp_table[i][j][k] = m
		return m
 
	elif i < r and k < b:
		m = solve(i+1,g,k+1) + (rl[i]*bl[k])	
		dp_table[i][j][k] = m
		return m
 
	elif j < g and k < b:
		m = solve(r,j+1,k+1) + (gl[j]*bl[k])
		dp_table[i][j][k] = m
		return m
	else:
		return 0

dp_table = [[[-1]*(b+1) for j in range(g+1)] for k in range(r+1)]
res = solve(0,0,0)
print(res)
