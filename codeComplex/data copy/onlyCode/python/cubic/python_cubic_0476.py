#!/usr/bin/env python3
import os
from sys import stdin
from math import inf

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solve(tc):
    N, M, K = map(int, stdin.readline().split())

    wx = [[] for j in range(N)]
    for i in range(N):
        wx[i] = list(map(int, stdin.readline().split()))

    wy = [[] for i in range(N-1)]
    for i in range(N-1):
        wy[i] = list(map(int, stdin.readline().split()))

    if K & 1:
        for i in range(N):
            for j in range(M):
                print(-1, end=' ')
            print()
        return

    mem = [[[0 for i in range(M)] for j in range(N)] for k in range(K+1)]

    half = K // 2
    for kk in range(1, half+1):
        for yy in range(N):
            for xx in range(M):
                mem[kk][yy][xx] = inf

                for d in range(4):
                    y = yy + dy[d]
                    x = xx + dx[d]

                    if y < 0 or y >= N or x < 0 or x >= M:
                        continue

                    if d == 0:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk-1][y][x] + wx[yy][xx]*2)
                    elif d == 1:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk-1][y][x] + wy[yy][xx]*2)
                    elif d == 2:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk-1][y][x] + wx[yy][x]*2)
                    else:
                        mem[kk][yy][xx] = min(
                            mem[kk][yy][xx], mem[kk-1][y][x] + wy[y][xx]*2)

    for yy in range(N):
        for xx in range(M):
            print(mem[half][yy][xx], end=' ')
        print()


tcs = 1
# tcs = int(stdin.readline().strip())
tc = 1
while tc <= tcs:
    solve(tc)
    tc += 1
