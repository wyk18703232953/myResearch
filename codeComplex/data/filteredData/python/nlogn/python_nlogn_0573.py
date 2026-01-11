import collections


def main(n):
    # Deterministically construct a rooted tree with n nodes (1..n)
    # Parent of node i (i>=2) is (i // 2), node 1 is the root with parent 0
    a = [0, 0]  # a[1] is unused, a[2..n] are parents
    for i in range(2, n + 1):
        a.append(i // 2)

    # construct tree
    G = collections.defaultdict(list)
    for i in range(2, len(a)):
        G[a[i]].append(i)

    # BFS to get nodes in topological order from root
    nodes = []
    q = collections.deque([1])
    while q:
        node = q.popleft()
        nodes.append(node)
        for v in G[node]:
            q.append(v)

    nodes.reverse()

    dp = {}
    for u in nodes:
        count = 0
        if len(G[u]) == 0:
            count += 1
        for v in G[u]:
            count += dp[v]
        dp[u] = count

    res = sorted(dp.values())
    # print(' '.join(map(str, res)))
    pass
if __name__ == "__main__":
    main(10)