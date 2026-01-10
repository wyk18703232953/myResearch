from collections import deque

def main(n):
    # Interpret n as the number of nodes m in a tree.
    # Build a deterministic tree and choose k deterministically from n.
    m = max(2, n)

    # Deterministically choose k based on m
    # For variety yet determinism, use k = m // 3 (at least 1)
    k = max(1, m // 3)

    G = [set() for _ in range(m + 1)]

    # Build a deterministic tree:
    # For 1 <= i < m, connect i with i+1 (path graph)
    for i in range(1, m):
        u, v = i, i + 1
        G[u].add(v)
        G[v].add(u)

    q, nq = deque(), deque()

    for u in range(1, m + 1):
        if len(G[u]) == 1:
            q.append(u)

    step = 0
    removed = 0
    ok = True

    while removed < m - 1 and q:
        each = {}
        for _ in range(len(q)):
            u = q.popleft()
            if not G[u]:
                continue
            nxt = next(iter(G[u]))
            G[u].remove(nxt)
            G[nxt].remove(u)
            each[nxt] = each.get(nxt, 0) + 1
            removed += 1
            if len(G[nxt]) == 0:
                break
            if len(G[nxt]) == 1:
                nq.append(nxt)
        if any(v < 3 for _, v in each.items()):
            ok = False
            break
        q, nq = nq, deque()
        step += 1

    if ok and step == k and removed == m - 1:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)