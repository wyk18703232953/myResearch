# Converted version of the original Codeforces 1100E solution
# with main(n) and internal random test generation (no input()).

import random
from typing import Dict, List, Tuple


def find_loop(g: List[List[int]], w: Dict[Tuple[int, int], int], k: int, n: int) -> bool:
    visited = [False] * n
    visited_int = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        stack = [g[i][:]]
        path = [i]
        visited[i] = True
        visited_int[i] = True
        while stack:
            if not stack[-1]:
                stack.pop()
                visited_int[path[-1]] = False
                path.pop()
                continue
            nxt = stack[-1][-1]
            stack[-1].pop()
            if w[(path[-1], nxt)] <= k:
                continue
            if visited_int[nxt]:
                return True
            if visited[nxt]:
                continue
            visited[nxt] = True
            visited_int[nxt] = True
            stack.append(g[nxt][:])
            path.append(nxt)
    return False


def top_sort(g: List[List[int]], w: Dict[Tuple[int, int], int], k: int, n: int) -> List[Tuple[int, int]]:
    visited = [False] * n
    order = [-1] * n
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        stack = [g[i][:]]
        path = [i]
        visited[i] = True
        while stack:
            if not stack[-1]:
                order[path[-1]] = cnt
                path.pop()
                stack.pop()
                cnt += 1
                continue
            nxt = stack[-1][-1]
            stack[-1].pop()
            if w[(path[-1], nxt)] <= k:
                continue
            if visited[nxt]:
                continue
            visited[nxt] = True
            stack.append(g[nxt][:])
            path.append(nxt)

    to_reverse = []
    for a, b in w.items():
        if b > k:
            continue
        if order[a[0]] < order[a[1]]:
            to_reverse.append(a)
    return to_reverse


def generate_test(n: int):
    """
    根据规模 n 生成测试数据：
    - 顶点数为 n
    - 边数随机：介于 n 到 n*(n-1) 的较小值之间（不包含自环）
    - 边权为 1..10^9 的随机整数
    返回 (n, m, g, w, w_tmp, kk)
    """
    if n <= 1:
        # 对于 n <= 1，图没有边
        m = 0
        g = [[] for _ in range(n)]
        w = {}
        w_tmp = {}
        kk = [0]
        return n, m, g, w, w_tmp, kk

    max_possible_edges = n * (n - 1)
    # 控制一下边数，避免极端完全图导致运行过慢
    max_edges_limit = min(max_possible_edges, n * 5)
    min_edges = min(n, max_edges_limit)
    m = random.randint(min_edges, max_edges_limit)

    g = [[] for _ in range(n)]
    w: Dict[Tuple[int, int], int] = {}
    w_tmp: Dict[Tuple[int, int], List[str]] = {}
    kk = [0]

    for i in range(1, m + 1):
        u = random.randint(1, n)
        v = random.randint(1, n)
        while v == u:
            v = random.randint(1, n)
        c = random.randint(1, 10**9)

        # 原代码是 1-based 输入，内部用 0-based
        u0, v0 = u - 1, v - 1
        g[u0].append(v0)

        # 边 (u0,v0) 的最大权重
        if (u0, v0) in w:
            w[(u0, v0)] = max(w[(u0, v0)], c)
        else:
            w[(u0, v0)] = c

        # 保存出现该有向边的 所有行号（边编号）
        if (u0, v0) in w_tmp:
            w_tmp[(u0, v0)].append(str(i))
        else:
            w_tmp[(u0, v0)] = [str(i)]

        kk.append(c)

    return n, m, g, w, w_tmp, kk


def main(n: int):
    # 1. 生成测试图
    n, m, g, w, w_tmp, kk = generate_test(n)

    # 2. 与原逻辑一致：二分答案 k
    kk.sort()
    l, r = 0, len(kk)

    if not find_loop(g, w, kk[l], n):
        print(0, 0)
        print()
        return

    if find_loop(g, w, kk[-1], n):
        kkk = kk[-1]
    else:
        while l + 1 != r:
            mid = (l + r) // 2
            if find_loop(g, w, kk[mid], n):
                l = mid
            else:
                r = mid
        kkk = kk[l + 1]

    to_reverse = top_sort(g, w, kkk, n)
    num = 0
    s: List[str] = []
    for t in to_reverse:
        num += len(w_tmp[t])
        s.extend(w_tmp[t])

    print(kkk, num)
    if s:
        print(" ".join(s))
    else:
        print()


# 示例：直接运行本文件时给一个默认规模
if __name__ == "__main__":
    main(5)