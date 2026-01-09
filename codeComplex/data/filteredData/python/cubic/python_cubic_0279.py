def solve(r, g, b, rs, gs, bs):
    rs.sort(reverse=True)
    gs.sort(reverse=True)
    bs.sort(reverse=True)
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    sol = 0
    for ri in range(r + 1):
        for gi in range(g + 1):
            for bi in range(b + 1):
                if ri < r and gi < g:
                    dp[ri + 1][gi + 1][bi] = max(dp[ri + 1][gi + 1][bi], rs[ri] * gs[gi] + dp[ri][gi][bi])
                if ri < r and bi < b:
                    dp[ri + 1][gi][bi + 1] = max(dp[ri + 1][gi][bi + 1], rs[ri] * bs[bi] + dp[ri][gi][bi])
                if gi < g and bi < b:
                    dp[ri][gi + 1][bi + 1] = max(dp[ri][gi + 1][bi + 1], gs[gi] * bs[bi] + dp[ri][gi][bi])
                sol = max(sol, dp[ri][gi][bi])
    return sol


def main(n):
    # Interpret n as total size; split into three groups
    if n < 3:
        n = 3
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # Deterministic data generation
    rs = [i + 1 for i in range(r)]
    gs = [2 * (i + 1) for i in range(g)]
    bs = [3 * (i + 1) for i in range(b)]

    ans = solve(r, g, b, rs, gs, bs)
    # print(ans)
    pass
if __name__ == "__main__":
    main(30)