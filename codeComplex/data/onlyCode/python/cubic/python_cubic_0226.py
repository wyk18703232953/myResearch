# https://codeforces.com/contest/1398/problem/D
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
# do magic here
sys.setrecursionlimit(200000)
r, g, b = map(int, input().split())
R = list(map(int, input().split()))
G = list(map(int, input().split()))
B = list(map(int, input().split()))
R.sort(reverse=True)
G.sort(reverse=True)
B.sort(reverse=True)

dp = [[[0 for i in range(b+5)] for j in range(g+5)] for k in range(r+5)]


def solve(i, j, k):
    x, y, z = 0, 0, 0
    if dp[i][j][k]:
        return dp[i][j][k]
    if i < r and j < g:
        x = (R[i] * G[j]) + solve(i+1, j+1, k)
    if i < r and k < b:
        y = (R[i] * B[k]) + solve(i+1, j, k+1)
    if j < g and k < b:
        z = (G[j] * B[k]) + solve(i, j+1, k+1)
    mx = max([x, y, z])
    dp[i][j][k] = mx
    return mx


print(solve(0, 0, 0))
