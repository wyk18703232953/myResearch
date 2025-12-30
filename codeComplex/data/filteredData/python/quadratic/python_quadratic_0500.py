import sys
import threading
import random

ans = []

def dfs(g, i, p):
    global ans
    count = 0
    for j in g[i]:
        if j == p:
            continue
        count += dfs(g, j, i)
    if count == 0:
        count = 1
    ans.append(count)
    return count

def solve(n):
    global ans
    ans = []

    # 生成一棵有 n 个节点的随机树，根为 1
    # l[i-1] 表示节点 i+1 的父节点
    if n <= 1:
        g = [[] for _ in range(n + 1)]
    else:
        parents = [random.randint(1, i) for i in range(1, n)]  # 长度 n-1，对应原来的 l
        g = [[] for _ in range(n + 1)]
        for i in range(1, n):
            g[i + 1].append(parents[i - 1])
            g[parents[i - 1]].append(i + 1)

    if n >= 1:
        dfs(g, 1, 0)
        ans.sort()
        print(' '.join(map(str, ans)))
    else:
        print("")

def main(n):
    max_recur_size = 10**5 * 2 + 1000
    max_stack_size = max_recur_size * 500

    sys.setrecursionlimit(max_recur_size)
    threading.stack_size(max_stack_size)
    thread = threading.Thread(target=solve, args=(n,))
    thread.start()
    thread.join()