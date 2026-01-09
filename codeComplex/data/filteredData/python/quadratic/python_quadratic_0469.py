def main(n):
    # Deterministic data generation
    # Interpret n as the size of arrays l and r
    # Create l and r so that the algorithm has meaningful work and usually succeeds
    # Example pattern:
    #   l[i] = i % (n // 2 + 1)
    #   r[i] = (n - 1 - i) % (n // 2 + 1)
    # This is arbitrary but fully deterministic.
    l = [i % (max(1, n // 2 + 1)) for i in range(n)]
    r = [(n - 1 - i) % (max(1, n // 2 + 1)) for i in range(n)]

    mp = {i: i for i in range(n)}
    out = [-1] * n
    v = 0

    a = n
    done = set()
    while v < n:
        ids = set()
        for j in range(n):
            if l[j] == 0 and r[j] == 0 and j not in done:
                ids.add(j)
                done.add(j)
        if len(ids) == 0:
            # print('NO')
            pass
            return
        v += len(ids)
        for i in ids:
            out[mp[i]] = a
            for j in range(len(l)):
                if j < i:
                    r[j] -= 1

                else:
                    l[j] -= 1
        a -= 1
    # print('YES')
    pass
    # print(' '.join(map(str, out)))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)