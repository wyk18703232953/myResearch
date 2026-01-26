def main(n):
    # Interpret n as total number of sticks; distribute to R, G, B as evenly as possible
    if n < 3:
        n = 3
    R = n // 3
    G = (n - R) // 2
    B = n - R - G

    # Deterministic generation of stick values, sorted in descending order
    # Use simple arithmetic progression and modular pattern
    r_vals = [float((i % 7) + 1) / ((i // 7) + 1) for i in range(R)]
    g_vals = [float((i % 5) + 2) / ((i // 5) + 2) for i in range(G)]
    b_vals = [float((i % 3) + 3) / ((i // 3) + 3) for i in range(B)]

    r_sticks = sorted(r_vals, reverse=True) + [0.0]
    g_sticks = sorted(g_vals, reverse=True) + [0.0]
    b_sticks = sorted(b_vals, reverse=True) + [0.0]

    # DP array
    dp = [[[0.0] * (B + 2) for _ in range(G + 2)] for _ in range(R + 2)]

    for ri in range(R + 1):
        for gi in range(G + 1):
            for bi in range(B + 1):
                v = dp[ri][gi][bi]
                rv = r_sticks[ri]
                gv = g_sticks[gi]
                bv = b_sticks[bi]
                if ri + 1 <= R and gi + 1 <= G:
                    nv = v + rv * gv
                    if nv > dp[ri + 1][gi + 1][bi]:
                        dp[ri + 1][gi + 1][bi] = nv
                if ri + 1 <= R and bi + 1 <= B:
                    nv = v + rv * bv
                    if nv > dp[ri + 1][gi][bi + 1]:
                        dp[ri + 1][gi][bi + 1] = nv
                if gi + 1 <= G and bi + 1 <= B:
                    nv = v + gv * bv
                    if nv > dp[ri][gi + 1][bi + 1]:
                        dp[ri][gi + 1][bi + 1] = nv

    ans = 0.0
    for r in range(R + 1):
        for g in range(G + 1):
            for b in range(B + 1):
                v = dp[r][g][b]
                if v > ans:
                    ans = v

    # print(int(ans + 1e-6))
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(30)