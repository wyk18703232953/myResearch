from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
import random

mod = 998244353
INF = float('inf')
p, u = "Petr", "Um_nik"

def comb(n, m): 
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0

def perm(n, m): 
    return factorial(n) // (factorial(n - m)) if n >= m else 0

def mdis(x1, y1, x2, y2): 
    return abs(x1 - x2) + abs(y1 - y2)

def ctd(chr): 
    return ord(chr) - ord("a")

def main(n: int):
    # 根据 n 生成测试数据：生成 1..n 的随机排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    vis = [0] * (n + 1)
    dic = {v: i + 1 for i, v in enumerate(arr)}

    sm = 0
    for i in range(1, n + 1):
        if vis[i] == 0:
            now = i
            vis[now] = 1

            while dic[now] != i:
                sm += 1
                now = dic[now]
                vis[now] = 1

    if (3 * n - sm) % 2 == 0:
        print(p)
    else:
        print(u)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)