'''
                ___                       ____                     
  ____ _____ _____/ (_)_  ______  ____ _____/ / /_  __  ______ ___  __
 / __ `/ __ `/ __  / / / / / __ \/ __ `/ __  / __ \/ / / / __ `/ / / /
/ /_/ / /_/ / /_/ / / /_/ / /_/ / /_/ / /_/ / / / / /_/ / /_/ / /_/ / 
\__,_/\__,_/\__,_/_/\__,_/ .___/\__,_/\__,_/_/ /_/\__, /\__,_/\__, /  
                        /_/                      /____/      /____/   
'''
import os.path
from math import gcd, floor, ceil
from collections import *
import sys
mod = 1000000007
INF = float('inf')
def st(): return list(sys.stdin.readline().strip())
def li(): return list(map(int, sys.stdin.readline().split()))
def mp(): return map(int, sys.stdin.readline().split())
def inp(): return int(sys.stdin.readline())
def pr(n): return sys.stdout.write(str(n)+"\n")
def prl(n): return sys.stdout.write(str(n)+" ")


if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve():
    n, m = mp()
    k = inp()
    l = li()
    q = deque()
    v = [[0]*(m+1) for i in range(n+1)]
    for i in range(0, 2*k - 1, 2):
        q.append((l[i], l[i+1]))
        v[l[i]][l[i+1]] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            A, B = a+dx[i], b+dy[i]
            if A > 0 and A <= n and B > 0 and B <= m:
                if not v[A][B]:
                    q.append((A, B))
                    v[A][B] = 1
    print(a, b)


for _ in range(1):
    solve()
