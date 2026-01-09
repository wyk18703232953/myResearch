def main(n):
    # Interpret n as the maximum node count; derive d and k deterministically
    # Ensure at least a minimal valid configuration
    if n < 3:
        n_effective = 3

    else:
        n_effective = n

    # Deterministic mapping from n to d and k
    # d: depth-like parameter, at least 1 and less than n_effective
    d = max(1, min(n_effective - 1, n_effective // 3))
    # k: branching factor-like parameter, at least 1
    k = max(1, (n_effective // 5) % (n_effective // 2 or 1))
    if k == 0:
        k = 1

    # Original logic starts here, with (n_effective, d, k) replacing input
    n0, d0, k0 = n_effective, d, k
    n, d, k = n0, d0, k0

    r, odd = divmod(d, 2)
    k -= 1
    cap = d + 1 if k == 1 else 1
    if k > 1:
        cap = 2 * (k ** (r + 1) - 1) // (k - 1) if odd else 1 + (k + 1) * (k ** r - 1) // (k - 1)
    if n == 1 or k < 1 < n - 1 or (k == 1 and d != n - 1) or d >= n or (k > 1 and not d < n <= cap):
        # print('NO')
        pass
        return

    def dfs(parent, depth):
        stack = []
        for _ in range(k - 1):
            child = rest.pop()
            res.append('%s %s' % (parent, child))
            if depth:
                stack.append((child, depth))
        while stack:
            parent2, depth2 = stack.pop()
            depth2 -= 1
            for _ in range(k):
                child = rest.pop()
                res.append('%s %s' % (parent2, child))
                if depth2:
                    stack.append((child, depth2))

    res = ['YES']
    for pc in enumerate(range(2, d + 2), 1):
        res.append('%d %d' % pc)
    rest = list(range(n, d + 1, -1))
    try:
        for p in range(r + 1, r + odd + 2):
            dfs(p, r - 1)
        for de, p, q in zip(range(r - 2, -1, -1), range(r, 1, -1), range(r + odd + 2, d + 1)):
            dfs(p, de)
            dfs(q, de)
    except IndexError:
        pass
    # print('\n'.join(res))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)