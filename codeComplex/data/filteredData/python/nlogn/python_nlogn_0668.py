import random
import sys


def find_loop(g, w, k, n):
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


def top_sort(g, w, k, n):
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


def main(n):
    """
    按规模 n 生成测试数据并执行原逻辑。
    生成规则：
      - 节点编号为 0..n-1
      - 随机生成 m 条边（这里设为 min(n*(n-1), 2*n)）
      - 边权为 [1, 100] 的随机整数
    输出与原程序一致：
      第一行：kkk num
      第二行：num 个边下标（从 1 开始）
    """

    # 生成随机图数据
    if n <= 1:
        print(0, 0)
        return

    max_possible_edges = n * (n - 1)
    m = min(max_possible_edges, 2 * n)  # 可根据需要调整边数规模

    edges = []
    for i in range(m):
        u = random.randrange(0, n)
        v = random.randrange(0, n)
        # 允许自环和多重边，保持与原代码能处理多重边的设定一致
        c = random.randint(1, 100)
        edges.append((u, v, c))

    # 以下逻辑与原 __main__ 中保持一致，只是使用生成的 edges
    w = {}
    g = [[] for _ in range(n)]
    w_tmp = {}
    kk = [0]

    for idx, (u, v, c) in enumerate(edges):
        g[u].append(v)
        if (u, v) in w:
            w[(u, v)] = max(w[(u, v)], c)
        else:
            w[(u, v)] = c
        if (u, v) in w_tmp:
            w_tmp[(u, v)].append(str(idx + 1))
        else:
            w_tmp[(u, v)] = [str(idx + 1)]
        kk.append(c)

    kk.sort()
    l, r = 0, len(kk)
    if not find_loop(g, w, kk[l], n):
        print(0, 0)
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
    s = []
    for t in to_reverse:
        num += len(w_tmp[t])
        s.extend(w_tmp[t])

    print(kkk, num)
    if num > 0:
        print(" ".join(s))


if __name__ == '__main__':
    # 示例：从命令行参数读取 n，若无则默认 n=5
    if len(sys.argv) > 1:
        n_arg = int(sys.argv[1])
    else:
        n_arg = 5
    main(n_arg)