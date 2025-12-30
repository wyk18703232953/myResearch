import random

def my_solve(n, m, graph, mask):
    if do_dfs_bool(n, graph, mask.copy()):
        c = get_cyclic(n, graph, mask)
        for u, v in c:
            graph[u].remove(v)
            if not do_dfs_bool(n, graph, mask.copy()):
                return 'YES'
            graph[u].append(v)
        return "NO"
    return "YES"

def get_cyclic(n, graph, mask):
    c, v = do_dfs(n, graph, mask)
    path = []
    begin = False
    if c:
        for u in c.keys():
            if c[u] == v:
                begin = True
                path.append((c[u], u))
            elif begin:
                path.append((c[u], u))
        tmp = list(c.keys())
        if len(tmp):
            path.append((tmp[-1], v))
    return path

def do_dfs_bool(n, graph, mask):
    colors = [0] * (n + 5)
    for u in graph.keys():
        if u not in mask.keys():
            if dfs_bool(u, graph, mask, colors):
                return True
    return False

def dfs_bool(u, graph, mask, colors):
    colors[u] = 1
    mask[u] = True
    for v in graph[u]:
        if colors[v] == 1:
            return True
        if colors[v] == 0:
            if dfs_bool(v, graph, mask, colors):
                return True
    colors[u] = 2
    return False

def do_dfs(n, graph, mask):
    colors = [0] * (n + 5)
    c = {}
    for u in graph.keys():
        if u not in mask.keys():
            c = {}
            p, v = dfs(u, graph, mask, c, colors)
            if p and v:
                return (p, v)
    return ({}, None)

def dfs(u, graph, mask, c, colors):
    colors[u] = 1
    for v in graph[u]:
        if colors[v] == 1:
            return (c, v)
        if colors[v] == 0:
            c[v] = u
            p, w = dfs(v, graph, mask, c, colors)
            if w:
                return (p, w)
    colors[u] = 2
    if len(c) > 0 and u in c.keys():
        del c[u]
    return (c, None)

def test(n, m, edges):
    graph = {}
    mask = {}
    for u, v in edges:
        if u not in graph.keys():
            graph[u] = []
        graph[u].append(v)
        if v not in graph.keys():
            graph[v] = []
    return my_solve(n, m, graph, mask)

def generate_edges(n):
    # 生成一个随机边集，可能包含环也可能无环
    max_edges = n * (n - 1)
    m = random.randint(0, max_edges)
    edges = set()
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v:
            edges.add((u, v))
    return list(edges)

def main(n):
    random.seed(0)
    edges = generate_edges(n)
    m = len(edges)
    return test(n, m, edges)

if __name__ == '__main__':
    # 示例调用：可自行修改 n
    result = main(5)
    print(result)