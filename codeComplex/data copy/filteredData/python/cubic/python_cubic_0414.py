def main(n):
    # Map n to grid size and k (even)
    if n < 2:
        n_rows = 1
        m_cols = 1
        k_steps = 2

    else:
        n_rows = n
        m_cols = n
        # choose k as smallest even >= n (but at least 2)
        k_steps = n if n % 2 == 0 else n + 1
        if k_steps < 2:
            k_steps = 2

    # Deterministic construction of A and B with positive integers
    A = [[0] * m_cols for _ in range(n_rows)]
    B = [[0] * m_cols for _ in range(n_rows)]

    # Original code read (n x (m-1)) for A's horizontal edges, stored shifted by +1
    # We generate deterministically: tmp[j] = (i + j + 1)
    for i in range(n_rows):
        tmp = [(i + j + 1) for j in range(m_cols - 1)]
        for j in range(m_cols - 1):
            A[i][j + 1] = tmp[j]

    # Original code read ((n-1) x m) for B's vertical edges, stored shifted by +1 in row
    # We generate deterministically: tmp[j] = (i + j + 1)
    for i in range(n_rows - 1):
        tmp = [(i + j + 1) for j in range(m_cols)]
        for j in range(m_cols):
            B[i + 1][j] = tmp[j]

    k = k_steps

    # Core algorithm (unchanged logic)
    if k % 2:
        ans = [[-1] * m_cols for _ in range(n_rows)]
        for a in ans:
            # print(*a)
            pass
        return

    ans = [[0] * m_cols for _ in range(n_rows)]
    lim = k // 2
    dp = [[[float("inf")] * (lim + 1) for _ in range(m_cols)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(m_cols):
            dp[i][j][0] = 0

    for step in range(1, lim + 1):
        for i in range(n_rows):
            for j in range(m_cols):
                if i:
                    dp[i][j][step] = min(dp[i][j][step], dp[i - 1][j][step - 1] + B[i][j])
                if j:
                    dp[i][j][step] = min(dp[i][j][step], dp[i][j - 1][step - 1] + A[i][j])
                if i < n_rows - 1:
                    dp[i][j][step] = min(dp[i][j][step], dp[i + 1][j][step - 1] + B[i + 1][j])
                if j < m_cols - 1:
                    dp[i][j][step] = min(dp[i][j][step], dp[i][j + 1][step - 1] + A[i][j + 1])

    for i in range(n_rows):
        for j in range(m_cols):
            ans[i][j] = dp[i][j][-1] * 2

    for a in ans:
        # print(*a)
        pass
if __name__ == "__main__":
    main(5)