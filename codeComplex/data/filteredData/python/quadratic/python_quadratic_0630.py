#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for _ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

# A 逻辑封装为可复用函数
def solve_A(a):
    n = len(a)
    a.sort()
    f = [1] * n
    p = 0
    ans = 0
    while p < n:
        while p < n and not f[p]:
            p += 1
        if p == n:
            break
        ans += 1
        for i in range(n):
            if a[i] % a[p] == 0:
                f[i] = 0
    return ans

def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的正整数数组
    # 这里生成 1 到 10*n 范围内的随机数
    random.seed(0)
    a = [random.randint(1, 10 * max(1, n)) for _ in range(n)]

    # 调用原本 A 的逻辑
    ans = solve_A(a)

    # 输出结果
    print(ans)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为测试规模
    main(10)