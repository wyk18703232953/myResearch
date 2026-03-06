def main(n):
    # Map n to matrix dimensions
    # For scalability, choose m = max(1, n // 2)
    # and rows = n
    rows = max(1, n)
    cols = max(1, n // 2)

    # Deterministic matrix generation
    # a[i][j] = (i * 131 + j * 17) % 1000000000
    a = [[(i * 131 + j * 17) % 1000000000 for j in range(cols)] for i in range(rows)]

    def get_ans(x):
        lim = 1 << cols
        match = lim - 1
        track = [-1 for _ in range(lim)]

        for i in range(rows):
            mask = 0
            for j in range(cols):
                if a[i][j] >= x:
                    mask |= 1 << j
            track[mask] = i

        for i in range(lim):
            if track[i] == -1:
                continue
            for j in range(lim):
                if track[j] == -1:
                    continue
                if (i | j) == match:
                    return track[i], track[j]

        return -1, -1

    lo = 0
    hi = 1000000000
    while lo < hi - 1:
        mid = (lo + hi) // 2
        i, j = get_ans(mid)
        if i == -1:
            hi = mid - 1
        else:
            lo = mid

    i, j = get_ans(hi)
    if i != -1:
        print(f"{i+1} {j+1}")
    else:
        i, j = get_ans(lo)
        print(f"{i+1} {j+1}")


if __name__ == "__main__":
    main(10)