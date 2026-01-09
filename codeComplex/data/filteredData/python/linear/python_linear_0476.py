def main(n):
    # Deterministic data generation based on n
    # c: costs, length n
    c = [(i * 7 + 3) % (10 ** 6) + 1 for i in range(n)]
    # a: permutation-like mapping with some structure, 0-based indices
    # create cycles of varying lengths deterministically
    a = [(i * 2 + 1) % n for i in range(n)]

    visited = [-1] * n
    res = 0

    for i in range(n):
        trace = []
        t = i
        mn = 10 ** 18
        while visited[t] == -1:
            visited[t] = i
            trace.append(t)
            t = a[t]

        if visited[t] != i:
            continue

        while trace:
            v = trace.pop()
            if c[v] < mn:
                mn = c[v]
            if t == v:
                break

        res += mn

    return res


if __name__ == "__main__":
    # example call for time-complexity experiments
    result = main(10**5)
    # print(result)
    pass