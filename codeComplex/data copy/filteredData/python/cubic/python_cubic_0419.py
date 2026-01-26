from math import inf

def main(n):
    # n controls grid size and k: n -> (rows, cols, steps)
    # Ensure at least 1x1 grid and even k
    rows = max(1, n)
    cols = max(1, n)
    # Make k even and scale with n
    k = 2 * max(1, n)

    # Deterministic generation of cosp and cosv based on indices
    cosp = [[(i + j + 1) for j in range(cols)] + [inf] for i in range(rows)]
    cosv = [[(i * j + 1) for j in range(cols)] for i in range(rows - 1)] + [[inf] * cols]

    if k % 2 == 1:
        for _ in range(rows):
            # print(*[-1] * cols)
            pass

    else:
        dp = [[0] * cols for _ in range(rows)]
        xx, yy = [0, 0, 1, -1], [1, -1, 0, 0]
        for _ in range(k // 2):
            dp1 = [[inf] * cols for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    for kk in range(4):
                        x1, y1 = i + xx[kk], j + yy[kk]
                        # Skip moves that go out of bounds
                        if not (0 <= x1 < rows and 0 <= y1 < cols):
                            continue
                        if kk < 2:
                            if kk == 1:
                                if j - 1 < 0:
                                    continue
                                edge = cosp[i][j - 1]

                            else:
                                edge = cosp[i][j]

                        else:
                            if kk == 3:
                                if i - 1 < 0:
                                    continue
                                edge = cosv[i - 1][j]

                            else:
                                edge = cosv[i][j]
                        if edge != inf:
                            dp1[i][j] = min(dp1[i][j], 2 * edge + dp[x1][y1])
            dp = [row[:] for row in dp1]
        for row in dp:
            # print(*row)
            pass
if __name__ == "__main__":
    main(5)