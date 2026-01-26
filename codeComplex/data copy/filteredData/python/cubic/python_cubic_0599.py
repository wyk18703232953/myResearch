def main(n):
    # Map n -> original parameters:
    # n_days = n
    # m (string length) = n
    # k (max removal operations) = n // 2
    n_days = n
    m = n
    k = n // 2

    # Deterministic generation of DATA: n binary strings of length m
    # Pattern: DATA[i][j] == '1' if (i + j) is even, else '0'
    DATA = []
    for i in range(n_days):
        s = ['1' if (i + j) % 2 == 0 else '0' for j in range(m)]
        DATA.append(''.join(s))

    INF = 1 << 60
    dp = [[INF] * (k + 10) for _ in range(n_days + 10)]
    dp[0][0] = 0

    COST = [[INF] * (k + 10) for _ in range(n_days + 10)]
    for i, string in enumerate(DATA):
        stack = []
        for j in range(m):
            if string[j] == "1":
                stack.append(j)
        L = len(stack)
        for j in range(k + 10):
            if j >= L:
                COST[i + 1][j] = 0

            else:
                for pos in range(j + 1):
                    l = pos
                    r = pos + L - 1 - j
                    cost_val = stack[r] - stack[l] + 1
                    if cost_val < COST[i + 1][j]:
                        COST[i + 1][j] = cost_val

    for day in range(1, n_days + 1):
        for used_cost in range(k + 1):
            best = INF
            row_cost = COST[day]
            prev_row = dp[day - 1]
            for prev_cost in range(used_cost + 1):
                val = prev_row[prev_cost] + row_cost[used_cost - prev_cost]
                if val < best:
                    best = val
            dp[day][used_cost] = best

    ans = min(dp[n_days][used_cost] for used_cost in range(k + 1))
    # print(ans)
    pass
if __name__ == "__main__":
    main(50)