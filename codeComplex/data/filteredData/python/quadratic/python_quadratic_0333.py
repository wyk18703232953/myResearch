def main(n):
    # Interpret n as the maximum number of nodes
    # Deterministically derive d and k from n with simple arithmetic
    if n <= 0:
        return

    # Ensure d >= 1 and not too large
    d = max(1, n // 4)
    # Ensure k >= 2 and at least enough to build a path
    k = max(2, min(5, n // 10 + 2))

    _min = d + 1

    if n < _min:
        # print('NO')
        pass

    else:
        res = []
        deg = [0] * (n + 1)
        dist = [0] * (n + 1)

        stack = []
        deg[1] = 1
        for i in range(1, d + 1):
            res.append((i, i + 1))
            if i > 1:
                deg[i] += 2
            dist[i] = max(i - 1, d + 1 - i)
        dist[d + 1] = d
        deg[d + 1] = 1

        for i in range(2, d + 1):
            stack.append(i)

        nxt = d + 2
        while stack:
            if nxt > n:
                break
            v = stack.pop()
            if dist[v] < d:
                while nxt <= n and deg[v] < k:
                    res.append((v, nxt))
                    deg[v] += 1
                    deg[nxt] += 1
                    dist[nxt] = dist[v] + 1
                    if dist[nxt] < d:
                        stack.append(nxt)
                    nxt += 1

        ok = nxt > n
        ok &= all(deg[i] <= k for i in range(1, n + 1))
        ok &= all(dist[i] <= d for i in range(1, n + 1))

        if not ok:
            # print('NO')
            pass

        else:
            # print('YES')
            pass
            for e in res:
                # print(*e)
                pass
if __name__ == "__main__":
    # Example deterministic call for experimental use
    main(20)