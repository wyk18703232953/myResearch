from math import inf

def main(n):
    # Map n to grid size and K
    # Choose n as rows; derive cols and K deterministically
    rows = max(1, n)
    cols = max(1, n)
    K = 2 * max(1, n // 2)  # ensure even K >= 2

    # Deterministic construction of hor and vert costs
    # hor: rows x (cols+1) but last is inf, original input had cols entries then + [inf]
    hor = []
    for i in range(rows):
        row = [(i + j) % 7 + 1 for j in range(cols)]  # small positive weights
        row.append(inf)
        hor.append(row)

    # vert: (rows-1) x cols then add last row of inf
    vert = []
    for i in range(rows - 1):
        row = [(i * 3 + j * 5) % 11 + 1 for j in range(cols)]
        vert.append(row)
    vert.append([inf] * cols)

    halfK = K // 2
    dp = [[[inf] * cols for _ in range(rows)] for _ in range(halfK + 1)]
    dp[0] = [[0] * cols for _ in range(rows)]

    def valid(i, j):
        return 0 <= i < rows and 0 <= j < cols

    for k in range(1, halfK + 1):
        prev = dp[k - 1]
        cur = dp[k]
        for i in range(rows):
            for j in range(cols):
                best = cur[i][j]
                if j + 1 < cols:
                    cand = prev[i][j + 1] + 2 * hor[i][j]
                    if cand < best:
                        best = cand
                if i + 1 < rows:
                    cand = prev[i + 1][j] + 2 * vert[i][j]
                    if cand < best:
                        best = cand
                if i - 1 >= 0:
                    cand = prev[i - 1][j] + 2 * vert[i - 1][j]
                    if cand < best:
                        best = cand
                if j - 1 >= 0:
                    cand = prev[i][j - 1] + 2 * hor[i][j - 1]
                    if cand < best:
                        best = cand
                cur[i][j] = best

    for row in dp[-1]:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)