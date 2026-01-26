def main(n):
    # Interpret n as the common size of a, b, c, capped by 200 due to dp size limit
    limit = 200
    size = min(max(0, n), limit)

    # Generate deterministic inputs
    # Original input structure: n, m, q on first line; three integer lists on following lines
    # Here we set n = m = q = size and construct a, b, c deterministically.
    n_val = size
    m_val = size
    q_val = size

    # Deterministic sequences; sorted in reverse to preserve original behavior
    a = sorted([i * 2 + 1 for i in range(n_val)], reverse=True)
    b = sorted([i * 3 + 2 for i in range(m_val)], reverse=True)
    c = sorted([i * 5 + 3 for i in range(q_val)], reverse=True)

    # DP array as in original program, fixed size 201
    dp = [[[0] * 201 for _ in range(201)] for _ in range(201)]

    for ijk in range(n_val + m_val + q_val + 1):
        for i in range(min(n_val + 1, ijk + 1)):
            # j is bounded by m_val and ijk - i
            max_j = min(m_val, ijk - i)
            for j in range(max_j + 1):
                k = ijk - i - j
                if k < 0 or k > q_val:
                    continue

                # Transition steps identical to original logic
                if i + 1 <= n_val:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                if j + 1 <= m_val:
                    dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])
                if k + 1 <= q_val:
                    dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k])
                if i + 1 <= n_val and j + 1 <= m_val:
                    dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k] + a[i] * b[j])
                if i + 1 <= n_val and k + 1 <= q_val:
                    dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k] + a[i] * c[k])
                if j + 1 <= m_val and k + 1 <= q_val:
                    dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k] + b[j] * c[k])

    result = dp[n_val][m_val][q_val]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)