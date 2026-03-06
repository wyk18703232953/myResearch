def check(x: int, a, m) -> (int, int):
    vis = {}
    for i, array in enumerate(a):
        t = 0
        for j, val in enumerate(array):
            if val >= x:
                t |= 1 << j
        vis[t] = i
    full = (1 << m) - 1
    if full in vis:
        return vis[full], vis[full]
    for i in range(1, full):
        if i not in vis:
            continue
        for j in range(1, full):
            if j in vis and (i | j) == full:
                return vis[i], vis[j]
    return -1, -1


def main(n: int):
    # Interpret n as the number of rows; keep columns small and fixed for determinism
    m = 5
    # Deterministic data generation: a[i][j] is a simple function of i and j
    a = [[(i + 1) * (j + 2) % 1000000000 for j in range(m)] for i in range(n)]

    l = 0
    r = int(1e9)
    res = (-1, -1)
    while l <= r:
        mid = (l + r) >> 1
        cur = check(mid, a, m)
        if cur != (-1, -1):
            res = cur
            l = mid + 1
        else:
            r = mid - 1
    ans = check(r, a, m)
    print(ans[0] + 1, ans[1] + 1)


if __name__ == "__main__":
    main(10)