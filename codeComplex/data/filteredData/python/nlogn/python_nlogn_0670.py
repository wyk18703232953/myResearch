from collections import deque

MAX = int(10e5 + 42)

def top_sort():
    global dag, top, g, n
    q = deque()
    cnt = 0

    for i in range(1, n + 1):
        if not dag[i]:
            q.append(i)

    while len(q):
        u_node = q.popleft()
        cnt += 1
        top[u_node] = cnt
        for to in g[u_node]:
            dag[to] -= 1
            if dag[to] == 0:
                q.append(to)
    return cnt == n

def check(mid):
    global n, m, g, u, v, c, dag
    for i in range(1, n + 1):
        g[i].clear()
        dag[i] = 0
    for i in range(1, m + 1):
        if c[i] > mid:
            g[u[i]].append(v[i])
            dag[v[i]] += 1
    return top_sort()

def main(n_input):
    global n, m, g, dag, top, u, v, c

    # Scale meaning:
    # n = number of nodes
    # m = number of edges, deterministically chosen as n * 2 (capped by MAX constraints)
    n = max(1, n_input)
    m = min(n * 2, MAX - 2)

    u, v, c = [0] * MAX, [0] * MAX, [0] * MAX
    g = [[] for _ in range(MAX)]
    dag = [0] * MAX
    top = [0] * MAX

    r = 0
    cnt = 0

    # Deterministic edge generation:
    # For i in [1..m]:
    #   u[i] = (i % n) + 1
    #   v[i] = ((i * 2) % n) + 1
    #   c[i] = i % (n + 1)
    # This may contain self-loops or parallel edges; logic is preserved.
    for i in range(1, m + 1):
        u[i] = (i % n) + 1
        v[i] = ((i * 2) % n) + 1
        c[i] = i % (n + 1)
        if c[i] > r:
            r = c[i]

    l = 0

    # Binary search
    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid

        else:
            l = mid + 1

    check(l)
    for i in range(1, m + 1):
        if c[i] <= l and top[v[i]] < top[u[i]]:
            cnt += 1

    # print(f"{l} {cnt}")
    pass
    for i in range(1, m + 1):
        if c[i] <= l and top[v[i]] < top[u[i]]:
            # print(i, end=" ")
            pass
    # print()
    pass
if __name__ == "__main__":
    main(1000)