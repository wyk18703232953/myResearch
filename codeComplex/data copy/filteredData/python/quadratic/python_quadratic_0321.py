def main(n):
    # Deterministically generate d, k based on n
    # Constraints derived from original logic:
    # - need d < n
    # - small-ish d, k but dependent on n
    if n < 3:
        # For too small n, just pick minimal valid parameters
        d = 1
        k = 2

    else:
        d = n // 3
        if d >= n:
            d = n - 1
        # ensure k >= maximum possible small degree; here choose around log n + 2
        k = (n.bit_length() + 2)

    # Now run the original algorithm with generated n, d, k
    from collections import deque

    if d >= n:
        # print("NO")
        pass
        return

    graph = [[] for _ in range(n + 1)]

    for i in range(1, d + 2):
        graph[i].append(min(i - 1, d + 1 - i))

    for i in range(1, d + 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)

    deg = [0] * (n + 1)
    deg[1] = 1
    deg[d + 1] = 1
    for i in range(2, d + 1):
        deg[i] = 2

    for x in deg:
        if x > k:
            # print("NO")
            pass
            return

    p = d + 2
    for i in range(1, d + 2):
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            while graph[x][0] > 0 and deg[x] < k and p <= n:
                graph[x].append(p)
                deg[x] += 1
                graph[p].append(graph[x][0] - 1)
                graph[p].append(x)
                deg[p] += 1
                q.append(p)
                p += 1

    if p <= n:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        vis = [-1] * (n + 1)

        for i in range(1, d + 2):
            if vis[i] == -1:
                q = deque()
                q.append(i)
                while q:
                    x = q.popleft()
                    vis[x] = 1
                    for j in range(1, len(graph[x])):
                        if vis[graph[x][j]] == -1:
                            # print(x, graph[x][j])
                            pass
                            q.append(graph[x][j])


if __name__ == "__main__":
    # Example deterministic call; change n to scale input size
    main(20)