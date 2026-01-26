def main(n):
    # Interpret n as the length of each array a, b, c BEFORE the "+1" in original code.
    # Original: n, m, v = map(lambda x: int(x) + 1, input().split())
    # Here we set n = m = v = n + 1 to keep the same structure.
    n_val = n + 1
    m_val = n + 1
    v_val = n + 1

    # Deterministic generation of arrays a, b, c of length n_val-1
    # Original code later does: a = [0] + a (so length becomes n_val)
    a = [i * 2 + 1 for i in range(n_val - 1)]
    b = [i * 3 + 2 for i in range(n_val - 1)]
    c = [i * 5 + 3 for i in range(n_val - 1)]

    # Sort in reverse as original
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # Prepend 0
    a = [0] + a
    b = [0] + b
    c = [0] + c

    # Initialize 3D dp array: dimensions [n_val][m_val][v_val]
    dp = [[[0] * v_val for _ in range(m_val)] for _ in range(n_val)]

    ans = 0
    for i in range(n_val):
        for j in range(m_val):
            for k in range(v_val):
                if i == j == k == 0:
                    continue
                if i == j == 0 or i == k == 0 or j == k == 0:
                    continue
                if i == 0:
                    dp[i][j][k] = dp[i][j - 1][k - 1] + b[j] * c[k]
                elif j == 0:
                    dp[i][j][k] = dp[i - 1][j][k - 1] + a[i] * c[k]
                elif k == 0:
                    dp[i][j][k] = dp[i - 1][j - 1][k] + a[i] * b[j]

                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j - 1][k] + a[i] * b[j],
                        dp[i - 1][j][k - 1] + a[i] * c[k],
                        dp[i][j - 1][k - 1] + b[j] * c[k],
                    )
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)