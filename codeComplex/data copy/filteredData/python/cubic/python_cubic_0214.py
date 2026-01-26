def main(n):
    # Map n to the sizes of the three arrays.
    # Here we choose a simple deterministic mapping:
    # rr + gg + bb <= n, and keep them balanced.
    rr = n // 3
    gg = n // 3
    bb = n - rr - gg

    inf = 114514

    # Deterministic generation of r, g, b using simple arithmetic patterns
    r = [i * 2 + 1 for i in range(rr)] + [inf]
    g = [i * 3 + 2 for i in range(gg)] + [inf]
    b = [i * 5 + 3 for i in range(bb)] + [inf]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # Allocate dp with dimensions (rr+1) x (gg+1) x (bb+1)
    dp = [[[0] * (bb + 1) for _ in range(gg + 1)] for _ in range(rr + 1)]

    ans = 0
    for i in range(rr + 1):
        ri = r[i]
        for j in range(gg + 1):
            gj = g[j]
            for k in range(bb + 1):
                bk = b[k]
                if (i + j + k) % 2:
                    continue
                dpijk = 0
                if i > 0 and j > 0:
                    val = dp[i - 1][j - 1][k] + ri * gj
                    if val > dpijk:
                        dpijk = val
                if j > 0 and k > 0:
                    val = dp[i][j - 1][k - 1] + gj * bk
                    if val > dpijk:
                        dpijk = val
                if k > 0 and i > 0:
                    val = dp[i - 1][j][k - 1] + bk * ri
                    if val > dpijk:
                        dpijk = val
                dp[i][j][k] = dpijk
                if ans < dpijk:
                    ans = dpijk

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(30)