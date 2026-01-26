import sys
import math
from itertools import product

n,m,k = [int(i) for i in sys.stdin.readline().split()]

horiz_costs = [[]]*n
vert_costs = [[]]*(n-1)

for i in range(n):
    horiz_costs[i] = [int(i) for i in sys.stdin.readline().split()]
for i in range(n-1):
    vert_costs[i] = [int(i) for i in sys.stdin.readline().split()]

if k%2 == 1:
    for _ in range(n):
        print(" ".join(["-1"]*m))
    quit()

ans = [[[0]*m for _ in range(n)] for _ in range(k//2+1)]

def costs(i,j,ans,time):
    r = []
    if j<m-1:
        r += [2*horiz_costs[i][j] + ans[time-1][i][j+1]]
    if j>0:
        r += [2*horiz_costs[i][j-1] + ans[time-1][i][j-1]]
    if i<n-1:
        r += [2*vert_costs[i][j] + ans[time-1][i+1][j]]
    if i>0:
        r += [2*vert_costs[i-1][j] + ans[time-1][i-1][j]]
    return r

for time in range(1, k//2+1):
    for i in range(n):
        for j in range(m):
            cost = costs(i,j,ans, time)
            for c in cost:
                if ans[time][i][j] == 0 or c < ans[time][i][j]:
                    ans[time][i][j] = c

for i in range(n):
    print(" ".join([str(s) for s in ans[-1][i]]))


