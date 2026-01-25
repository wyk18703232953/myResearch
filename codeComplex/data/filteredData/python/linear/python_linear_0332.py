def main(n):
    # Interpret n as:
    # n: number of existing toggle points
    # M: total length of the interval [0, M]
    # Here we set M = 2 * n to scale linearly with n
    if n <= 0:
        # Degenerate case: no toggles, light off all the time
        print(0)
        return

    M = 2 * n

    # Construct a deterministic, strictly increasing sequence of toggle points in [1, M-1]
    # Example: positions at 1, 2, ..., n (clipped to M-1)
    a_inner = [min(i, M - 1) for i in range(1, n + 1)]
    # Ensure strict increase and within bounds
    filtered = []
    last = 0
    for x in a_inner:
        if x > last and x < M:
            filtered.append(x)
            last = x
    a_inner = filtered
    n = len(a_inner)

    a = [0] + a_inner + [M]

    # Core logic from original testcase()
    ontime = [0] * (n + 1)
    tmp = 0
    for ind in range(n, -1, -1):
        if ind % 2 == 0:  # light will be on from now
            tmp += a[ind + 1] - a[ind]  # total ontime from ind
        ontime[ind] = tmp

    mx = ontime[0]
    for ind in range(n + 1):  # iterate over segments
        l, r = a[ind], a[ind + 1]
        if r - l <= 1:
            continue
        for x in (l + 1, r - 1):
            newtime = ontime[0] - ontime[ind]
            if ind % 2 == 0:
                newtime += x - l
            else:
                newtime += r - x
            newtime += (M - r) - ontime[ind]
            mx = max(mx, newtime)

    print(mx)


if __name__ == "__main__":
    # Example deterministic call for complexity experiment
    main(10)