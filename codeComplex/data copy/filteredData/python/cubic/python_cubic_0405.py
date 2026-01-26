def main(n):
    # Interpret n as grid size; ensure at least 2x2 and even k>=2
    if n < 2:
        n = 2
    rows = n
    cols = n
    k = 2 * ((n % 5) + 1)  # deterministic even k in [2,10]

    # Deterministically generate a (rows x cols) and b ((rows-1) x cols)
    a = [[(i * cols + j) % 7 + 1 for j in range(cols)] for i in range(rows)]
    if rows > 1:
        b = [[(i * cols + j) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    else:
        b = []

    m = cols

    # Core logic from original program
    if k % 2:
        ans = [-1] * m
        for _ in range(rows):
            # print(*ans)
            pass
        return

    G = [[] for _ in range(rows * m + 1)]
    for i in range(rows):
        a0 = a[i]
        for j in range(m - 1):
            x = a0[j]
            G[i * m + j].append((i * m + j + 1, x))
            G[i * m + j + 1].append((i * m + j, x))
    for i in range(rows - 1):
        b0 = b[i]
        for j in range(m):
            x = b0[j]
            G[i * m + j].append(((i + 1) * m + j, x))
            G[(i + 1) * m + j].append((i * m + j, x))

    dp = [0] * (rows * m)
    dp0 = [0] * (rows * m)
    inf = 1145141919
    for i in range(rows):
        for j in range(m):
            s = i * m + j
            dps = inf
            for t, x in G[s]:
                dps = min(dps, 2 * x)
            dp[s] = dps
            dp0[s] = dps

    for _ in range((k - 2) // 2):
        dp1 = [0] * (rows * m)
        for i in range(rows):
            for j in range(m):
                s = i * m + j
                dps = dp0[s] + 2 * dp[s]
                for t, x in G[s]:
                    dps = min(dps, 2 * x + dp0[t])
                dp1[s] = dps
        dp0 = dp1

    for i in range(rows):
        ans = dp0[(m * i):(m * (i + 1))]
        # print(*ans)
        pass
if __name__ == "__main__":
    main(5)