import random

def matching(n, m, path):
    # Hopcroft–Karp O(E * V^0.5)
    match1 = [-1] * n
    match2 = [-1] * m

    # Greedy initialization
    for node in range(n):
        for nei in path[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break

    while True:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in path[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in path]
        dfs = [node for node in range(n) if depth[node] == 0]

        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = path[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()

    return n - match1.count(-1)


def generate_test_data(n):
    """
    生成测试数据：
    顶点编号为 0..n-1，随机生成边集合 edg（无自环、无重边）。
    """
    max_edges = n * n
    # 控制边数在 [n, min(max_edges, 3n)] 范围内，确保有一定稠密度但不至于太大
    m = random.randint(n, min(max_edges, 3 * n)) if n > 0 else 0

    edges_set = set()
    while len(edges_set) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u == v:
            continue
        if (u, v) in edges_set:
            continue
        edges_set.add((u, v))

    edg = list(edges_set)
    return n, len(edg), edg


def main(n):
    """
    n 为规模参数：图有 n 个顶点（0..n-1），边由 generate_test_data(n) 随机生成。
    返回原程序计算得到的最小代价 ans。
    """
    n, m, edg = generate_test_data(n)

    ans = float("inf")
    for centre in range(n):
        path = [[] for _ in range(n)]
        cost = 2 * n - 1
        extra = m
        for u, v in edg:
            if u == centre or v == centre:
                cost -= 1
                extra -= 1
            else:
                path[u].append(v)

        maxMatch = matching(n, n, path)
        extra -= maxMatch
        cost += n - 1 - maxMatch + extra
        ans = min(ans, cost)
    return ans


# 示例：直接运行本文件时，用一个固定规模调用 main 并打印结果。
if __name__ == "__main__":
    random.seed(0)  # 保证可复现
    n_example = 10
    result = main(n_example)
    print(result)