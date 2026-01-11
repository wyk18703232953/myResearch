from collections import defaultdict, deque

def judge(x, n, edges):
    ins = [0] * n
    outs = defaultdict(list)

    for u, v, c in edges:
        if c > x:
            ins[v] += 1
            outs[u].append(v)

    q = deque([v for v in range(n) if ins[v] == 0])
    cnt = 0

    while q:
        v = q.popleft()
        cnt += 1

        for nv in outs[v]:
            ins[nv] -= 1
            if ins[nv] == 0:
                q.append(nv)

    return cnt == n

def binary_search(n, edges):
    l, r = 0, 10**9 + 10

    while l <= r:
        m = (l + r) // 2
        if judge(m, n, edges):
            r = m - 1

        else:
            l = m + 1

    return l

def generate_data(n):
    if n < 2:
        n_nodes = 2

    else:
        n_nodes = n
    m_edges = n_nodes * 2

    edges = []
    idx = defaultdict(lambda: deque([]))

    # Deterministic edge generation:
    # First create a chain to keep graph structure simple and scalable
    edge_counter = 1
    for i in range(n_nodes - 1):
        u = i
        v = i + 1
        c = (i * 3 + 5) % (10**6)
        edges.append((u, v, c))
        key = 10**6 * u + v
        idx[key].append(edge_counter)
        edge_counter += 1

    # Add additional edges in a deterministic but bounded way
    extra_edges = m_edges - (n_nodes - 1)
    for i in range(extra_edges):
        u = i % n_nodes
        v = (i * 2 + 1) % n_nodes
        if u == v:
            v = (v + 1) % n_nodes
        c = (i * i + 7 * i + 11) % (10**6)
        edges.append((u, v, c))
        key = 10**6 * u + v
        idx[key].append(edge_counter)
        edge_counter += 1

    return n_nodes, m_edges, edges, idx

def main(n):
    n_nodes, m, edges, idx = generate_data(n)

    k = binary_search(n_nodes, edges)
    ins = [0] * n_nodes
    outs = defaultdict(list)
    removed = []

    for u, v, c in edges:
        if c > k:
            ins[v] += 1
            outs[u].append(v)

        else:
            removed.append((u, v))

    q = deque([v for v in range(n_nodes) if ins[v] == 0])
    order = [-1] * n_nodes
    cnt = 0

    while q:
        v = q.popleft()
        order[v] = cnt
        cnt += 1

        for nv in outs[v]:
            ins[nv] -= 1
            if ins[nv] == 0:
                q.append(nv)

    change = []
    for u, v in removed:
        if order[v] < order[u]:
            change.append(idx[10**6 * u + v].popleft())

    # print(k, len(change))
    pass

    if change:
        # print(*change)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)