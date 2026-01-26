def main(n):
    # Ensure n is at least 3 so that the algorithm (which uses borders) has room
    if n < 3:
        n = 3
    m = n

    # Deterministic matrix generation.
    # Pattern: cell is '*' (1) if (i * 131 + j * 17) % 7 < 3 else '.' (0)
    mat = []
    for i in range(n):
        row = []
        for j in range(m):
            v = (i * 131 + j * 17) % 7
            row.append(1 if v < 3 else 0)
        mat.append(row)

    ver = [[0 for _ in range(m)] for _ in range(n)]
    hor = [[0 for _ in range(m)] for _ in range(n)]

    dp = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            x, y = n - i - 1, m - j - 1
            if mat[i][j] == 1:
                dp[i][j][0] = max(dp[i][j - 1][0], mat[i][j - 1]) + 1
                dp[i][j][1] = max(dp[i - 1][j][1], mat[i - 1][j]) + 1
            if mat[x][y] == 1:
                dp[x][y][2] = max(dp[x][y + 1][2], mat[x][y + 1]) + 1
                dp[x][y][3] = max(dp[x + 1][y][3], mat[x + 1][y]) + 1

    stars = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if mat[i][j] == 1:
                s = min(dp[i][j]) - 1
                if s > 0:
                    stars.append((i + 1, j + 1, s))
                    ver[i - s][j] += 1
                    if i + s + 1 < n:
                        ver[i + s + 1][j] -= 1
                    hor[i][j - s] += 1
                    if j + s + 1 < m:
                        hor[i][j + s + 1] -= 1

    for i in range(1, n):
        for j in range(1, m):
            ver[i][j] += ver[i - 1][j]
            hor[i][j] += hor[i][j - 1]

    chk = True
    for i in range(n):
        for j in range(m):
            if mat[i][j] and max(ver[i][j], hor[i][j]) <= 0:
                chk = False
                break
        if not chk:
            break

    if chk:
        # print(len(stars))
        pass
        for s in stars:
            # print(*s)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)