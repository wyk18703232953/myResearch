def main(n):
    # Interpret n as grid size: n x n grid, k = n
    rows = n
    cols = n
    k = n

    # Deterministically generate dist1 and dist2 based on indices
    # dist1: rows x (cols-1)
    dist1 = []
    for i in range(rows):
        row = []
        for j in range(cols - 1):
            # simple deterministic positive weights
            row.append((i + 1) + (j + 1))
        dist1.append(row)

    # dist2: (rows-1) x cols
    dist2 = []
    for i in range(rows - 1):
        row = []
        for j in range(cols):
            row.append((i + 1) * (j + 2))
        dist2.append(row)

    n_local = rows
    m_local = cols

    if k % 2:
        # print(' '.join(map(str, [-1] * (n_local * m_local))))
        pass
        return

    k //= 2
    dp = [10**9] * ((k + 1) * n_local * m_local)
    for i in range(n_local):
        for j in range(m_local):
            dp[i * m_local + j] = 0

    for t in range(k):
        r = (t + 1) * n_local * m_local
        q = t * n_local * m_local
        for i in range(n_local):
            for j in range(m_local):
                base_idx = q + i * m_local + j
                if i < n_local - 1:
                    idx = r + (i + 1) * m_local + j
                    val = dp[base_idx] + 2 * dist2[i][j]
                    if val < dp[idx]:
                        dp[idx] = val
                if i > 0:
                    idx = r + (i - 1) * m_local + j
                    val = dp[base_idx] + 2 * dist2[i - 1][j]
                    if val < dp[idx]:
                        dp[idx] = val
                if j < m_local - 1:
                    idx = r + i * m_local + (j + 1)
                    val = dp[base_idx] + 2 * dist1[i][j]
                    if val < dp[idx]:
                        dp[idx] = val
                if j > 0:
                    idx = r + i * m_local + (j - 1)
                    val = dp[base_idx] + 2 * dist1[i][j - 1]
                    if val < dp[idx]:
                        dp[idx] = val

    ans = []
    base = k * n_local * m_local
    for i in range(n_local):
        for j in range(m_local):
            ans.append(dp[base + i * m_local + j])
    # print(' '.join(map(str, ans)))
    pass
if __name__ == "__main__":
    main(5)