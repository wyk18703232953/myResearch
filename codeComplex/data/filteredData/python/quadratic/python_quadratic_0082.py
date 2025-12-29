import random


def prepare(n, adj, deg):
    stack = [i for i in range(n) if deg[i] == 0]
    cnt = 0
    while stack:
        v = stack.pop()
        cnt += 1
        for dest in adj[v]:
            deg[dest] -= 1
            if deg[dest] == 0:
                stack.append(dest)
        adj[v].clear()
    return cnt == n


def solve(st, n, m, adj, deg):
    stack = [st]
    visited = [0] * n
    cnt = 0
    while stack:
        v = stack.pop()
        cnt += 1
        for dest in adj[v]:
            if dest == st:
                continue
            visited[dest] += 1
            if deg[dest] == visited[dest]:
                stack.append(dest)
    return cnt == m


def gen_test_data(n):
    # 生成一个随机有向图，节点编号为 0..n-1
    # 保证无自环（可以修改为允许自环）
    max_edges = n * (n - 1)
    # 控制边数规模，这里取 0.3 * 完全图边数，至少 1 条
    m = max(1, min(max_edges, int(max_edges * 0.3)))
    edges = set()
    while len(edges) < m:
        u = random.randrange(n)
        v = random.randrange(n)
        if u == v:
            continue
        edges.add((u, v))
    return list(edges)


def main(n):
    edges = gen_test_data(n)
    m = len(edges)

    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    deg = [0] * n

    for u, v in edges:
        adj[u].append(v)
        rev[v].append(u)
        deg[v] += 1

    if prepare(n, adj, deg):
        print("YES")
        return

    # 重新计算剩余有入度的边数
    m_remain = sum(1 for i in range(n) if deg[i] > 0)
    if m_remain == 0:
        print("NO")
        return

    for i in range(n):
        if deg[i] == 1 and solve(i, n, m_remain, adj, deg):
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)