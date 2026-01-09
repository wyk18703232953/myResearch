import sys
from math import inf

def main(n):
    # Map n to grid size and step count
    # Choose n = number of cells; make grid as square as possible
    if n <= 0:
        return
    m = int(n ** 0.5)
    if m * m < n:
        m += 1
    rows = m
    cols = m
    # Derive k from n in a deterministic way; ensure even
    k = max(2, (n // 2) * 2)

    # Build A and B using deterministic formulas
    A = [[0] * cols for _ in range(rows)]
    B = [[0] * cols for _ in range(rows)]

    # Original meaning:
    # A[i][j+1] is cost to move horizontally between (i,j) and (i,j+1)
    # B[i+1][j] is cost to move vertically between (i,j) and (i+1,j)
    for i in range(rows):
        # tmp length = cols-1 for horizontal edges in row i
        tmp = [(i + 1) * (j + 2) % 7 + (i + j) % 5 + 1 for j in range(cols - 1)]
        for j in range(cols - 1):
            A[i][j + 1] = tmp[j]

    for i in range(rows - 1):
        # tmp length = cols for vertical edges between row i and i+1
        tmp = [(i + 2) * (j + 1) % 9 + (i + j) % 3 + 1 for j in range(cols)]
        for j in range(cols):
            B[i + 1][j] = tmp[j]

    if k % 2:
        for _ in range(rows):
            # print(*([-1] * cols))
            pass
        return

    lim = k // 2
    dp = [[[inf] * (lim + 1) for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            dp[i][j][0] = 0

    for step in range(1, lim + 1):
        for i in range(rows):
            for j in range(cols):
                cur = dp[i][j][step]
                if i:
                    cost = dp[i - 1][j][step - 1] + B[i][j]
                    if cost < cur:
                        cur = cost
                if j:
                    cost = dp[i][j - 1][step - 1] + A[i][j]
                    if cost < cur:
                        cur = cost
                if i < rows - 1:
                    cost = dp[i + 1][j][step - 1] + B[i + 1][j]
                    if cost < cur:
                        cur = cost
                if j < cols - 1:
                    cost = dp[i][j + 1][step - 1] + A[i][j + 1]
                    if cost < cur:
                        cur = cost
                dp[i][j][step] = cur

    ans = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            ans[i][j] = dp[i][j][lim] * 2

    for row in ans:
        # print(*row)
        pass
if __name__ == "__main__":
    # Example deterministic call
    main(25)