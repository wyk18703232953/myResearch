import random

def main(n):
    # 随机生成一个 n x n 的网格，包含 '*' 和 '.'
    m = n
    mat = []
    for _ in range(n):
        row = [random.choice(['*', '.']) for _ in range(m)]
        mat.append([1 if c == '*' else 0 for c in row])

    ver = [[0 for _ in range(m)] for _ in range(n)]
    hor = [[0 for _ in range(m)] for _ in range(n)]

    # dp[i][j][0]: 从左往右，当前点向左的长度
    # dp[i][j][1]: 从上往下，当前点向上的长度
    # dp[i][j][2]: 从右往左，当前点向右的长度
    # dp[i][j][3]: 从下往上，当前点向下的长度
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
        print(len(stars))
        for s in stars:
            print(*s)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10) 生成 10x10 的随机测试数据并运行
    main(10)