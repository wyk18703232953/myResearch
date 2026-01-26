import sys
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s.rstrip()))
def invr():
    return(map(int,input().split()))
n, m, k=inlt()
M=[[[] for i in range(m)] for j in range(n)]
S=[[-1]*m for i in range(n)]
for y in range(n):
	L=inlt()
	for x in range(m-1):
		M[y][x].append(((y, x+1), L[x]))
		M[y][x+1].append(((y, x), L[x]))

for y in range(n-1):
	L=inlt()

	for x in range(m):
		M[y][x].append(((y+1, x), L[x]))
		M[y+1][x].append(((y, x), L[x]))
if k%2==0:
	for l in range(k//2):
		S2=[[0]*m for i in range(n)]
		for y in range(n):
			for x in range(m):
				Mi=10000000000000000000000
				for ((a, b), p) in M[y][x]:
					Mi=min(Mi,max(0,S[a][b])+p)
				S2[y][x]=Mi
		S=S2
	for y in range(n):
		for x in range(m):
			S[y][x]*=2

for y in range(n):
	print(' '.join(list(map(str, S[y]))))