import math

def main(n):
    # Map n to grid size and step count:
    # For scalability, let grid be approximately sqrt(n) x sqrt(n),
    # and let k be an even number up to 20 (since dp third dimension is size 22).
    if n <= 0:
        return
    s = int(n ** 0.5)
    if s < 1:
        s = 1
    max_dim = 50  # avoid excessive memory for very large n
    n_rows = min(s, max_dim)
    n_cols = min(s, max_dim)
    # Ensure k is even and within 2..20
    k = min(2 * ((n // 2) % 10 + 1), 20)

    horz = []
    vert = []

    if k & 1:
        for _ in range(n_rows):
            temp = [-1 for _ in range(n_cols)]
            # print(*temp)
            pass
        return

    else:
        # Deterministically generate horz (n_rows x n_cols-1) and vert (n_rows-1 x n_cols)
        for i in range(n_rows):
            row = [(i + j + 1) for j in range(n_cols - 1)]
            horz.append(row)
        for i in range(n_rows - 1):
            row = [(2 * i + j + 1) for j in range(n_cols)]
            vert.append(row)

        dp = [[[0 for _ in range(22)] for _ in range(n_cols)] for _ in range(n_rows)]

        for x in range(2, k + 1, 2):
            for i in range(n_rows):
                for j in range(n_cols):
                    dp[i][j][x] = math.inf
                    if i > 0:
                        dp[i][j][x] = min(dp[i][j][x], dp[i - 1][j][x - 2] + 2 * vert[i - 1][j])
                    if i < n_rows - 1:
                        dp[i][j][x] = min(dp[i][j][x], dp[i + 1][j][x - 2] + 2 * vert[i][j])
                    if j > 0:
                        dp[i][j][x] = min(dp[i][j][x], dp[i][j - 1][x - 2] + 2 * horz[i][j - 1])
                    if j < n_cols - 1:
                        dp[i][j][x] = min(dp[i][j][x], dp[i][j + 1][x - 2] + 2 * horz[i][j])

        for i in range(n_rows):
            temp = []
            for j in range(n_cols):
                temp.append(dp[i][j][k])
            # print(*temp)
            pass
if __name__ == "__main__":
    main(1000)