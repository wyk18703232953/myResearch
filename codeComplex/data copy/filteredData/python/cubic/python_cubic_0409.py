def main(n):
    # Interpret n as both number of rows and columns for scalability
    rows = n
    cols = n

    # Deterministic mapping from n to k (must be even to avoid trivial branch)
    # Ensure k >= 2 and even
    k = max(2, (n % 10) * 2)

    # Generate A (rows x cols) and B ((rows-1) x cols) deterministically
    # A[i][j] = (i + j + 1) for example
    A = [[i + j + 1 for j in range(cols)] for i in range(rows)]
    # B[i][j] = (i * cols + j + 1)
    if rows > 1:
        B = [[i * cols + j + 1 for j in range(cols)] for i in range(rows - 1)]

    else:
        B = []

    inf = float('inf')

    if k % 2:
        ans = [[-1] * cols for _ in range(rows)]
        for row in ans:
            # print(*row)
            pass
        return

    dp = [[inf] * cols for _ in range(rows)]
    ans = [[None] * cols for _ in range(rows)]

    half_k = k // 2
    for l in range(half_k + 1):
        new_dp = [[inf] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if l == 0:
                    new_dp[i][j] = 0
                    continue

                up = B[i - 1][j] * 2 + dp[i - 1][j] if i - 1 >= 0 and rows > 1 else inf
                right = A[i][j] * 2 + dp[i][j + 1] if j + 1 < cols else inf
                left = A[i][j - 1] * 2 + dp[i][j - 1] if j - 1 >= 0 else inf
                down = B[i][j] * 2 + dp[i + 1][j] if i + 1 < rows and rows > 1 else inf

                new_dp[i][j] = min(up, right, left, down)
                if l == half_k:
                    ans[i][j] = new_dp[i][j]
        dp = new_dp

    for row in ans:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)