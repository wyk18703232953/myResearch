# -*- coding: utf-8 -*-

import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
# sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

def check(x):
    T1 = T[:x] + '*'
    T2 = T[x:] + '*'
    m1 = len(T1)
    m2 = len(T2)

    dp = list2d(N+1, m1, -1)
    dp[0][0] = 0
    for i in range(N):
        s = S[i]
        for j in range(m1):
            k = dp[i][j]
            if k != -1:
                dp[i+1][j] = max(dp[i+1][j], k)
                if T1[j] == s:
                    dp[i+1][j+1] = max(dp[i+1][j+1], k)
                if T2[k] == s:
                    dp[i+1][j] = max(dp[i+1][j], k+1)
    return dp[N][m1-1] == m2-1

for _ in range(INT()):
    S = input()
    T = input()

    N = len(S)
    M = len(T)
    for x in range(M):
        if check(x):
            YES()
            break
    else:
        NO()
