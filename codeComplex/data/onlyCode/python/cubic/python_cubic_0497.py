from sys import stdin, stdout
import heapq
from collections import defaultdict
import math
import bisect




def main():
    n,m,k = list(map(int, stdin.readline().split()))
    right = []
    for _ in range(n):
        right.append(list(map(int, stdin.readline().split())))
    down = []
    for _ in range(n-1):
        down.append(list(map(int, stdin.readline().split())))
    if k % 2 == 1:
        for _ in range(n):
            stdout.write(" ".join(["-1" for _ in range(m)])+"\n")
        return
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(1, (k//2) + 1):
        tmp = [[math.inf for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    tmp[i][j] = min(tmp[i][j], dp[i-1][j] + 2 * down[i-1][j])
                if i < n-1:
                    tmp[i][j] = min(tmp[i][j], dp[i + 1][j] + 2 * down[i][j])
                if j:
                    tmp[i][j] = min(tmp[i][j], dp[i][j - 1] + 2 * right[i][j - 1])
                if j < m-1:
                    tmp[i][j] = min(tmp[i][j], dp[i][j + 1] + 2 * right[i][j])
        dp = tmp
        #print(dp)
    for i in range(n):
        stdout.write(" ".join([str(x) for x in dp[i]]) + "\n")

main()