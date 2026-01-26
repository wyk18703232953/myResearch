def main(n):
    high = 10 ** 12

    # Map n to grid dimensions and k (even)
    # Choose m = n, k = 2 * n (so k grows with n and is even)
    m = n if n > 0 else 1
    k = 2 * n
    if k % 2:
        k += 1
    original_k = k

    # Deterministic generation of hozs (n x (m-1)) and verts ((n-1) x m)
    hozs = []
    for i in range(n):
        row = []
        for j in range(m - 1):
            row.append((i * m + j) % 10 + 1)
        hozs.append(row)

    verts = []
    for i in range(n - 1):
        row = []
        for j in range(m):
            row.append((i * m + j * 2) % 10 + 1)
        verts.append(row)

    if original_k % 2:
        for _ in range(n):
            # print("-1 " * m)
            pass
        return

    k = original_k // 2

    dp = []
    for i in range(n):
        dp.append([])
        for j in range(m):
            dp[-1].append([0] * (k + 1))

    for depth in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                if i == 0:
                    up = high

                else:
                    up = verts[i - 1][j] + dp[i - 1][j][depth - 1]
                if i == n - 1:
                    down = high

                else:
                    down = verts[i][j] + dp[i + 1][j][depth - 1]
                if j == 0:
                    left = high

                else:
                    left = hozs[i][j - 1] + dp[i][j - 1][depth - 1]
                if j == m - 1:
                    right = high

                else:
                    right = hozs[i][j] + dp[i][j + 1][depth - 1]
                min_cost = min(up, down, left, right)
                dp[i][j][depth] += min_cost

    for i in range(n):
        # print(*[2 * dp[i][j][k] for j in range(m)])
        pass
if __name__ == "__main__":
    main(5)