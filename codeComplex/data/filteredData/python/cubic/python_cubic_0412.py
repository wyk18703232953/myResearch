import random

def helper(n, m, k, hedge, vedge):
    if k % 2 == 1:
        return [[-1] * m for _ in range(n)]

    k //= 2
    pool = [[[0] * m for _ in range(n)] for _ in range(k + 1)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for t in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                tres = [9999999] * 4
                for c in range(4):
                    ni, nj = i + dx[c], j + dy[c]
                    if 0 <= ni < n and 0 <= nj < m:
                        if c == 0:      # right
                            tres[c] = hedge[i][j] * 2 + pool[t - 1][ni][nj]
                        elif c == 1:    # left
                            tres[c] = hedge[i][j - 1] * 2 + pool[t - 1][ni][nj]
                        elif c == 2:    # down
                            tres[c] = vedge[i][j] * 2 + pool[t - 1][ni][nj]
                        else:           # up
                            tres[c] = vedge[i - 1][j] * 2 + pool[t - 1][ni][nj]
                pool[t][i][j] = min(tres)

    return pool[k]


def main(n):
    # 根据规模 n 生成测试数据
    # 这里令 m = n，k = 2*n，边权在 [1, 10] 内随机生成
    m = n
    k = 2 * n

    random.seed(0)
    hedge = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    vedge = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    res = helper(n, m, k, hedge, vedge)
    for row in res:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    # 示例：调用 main(4) 可测试规模为 4 的数据
    main(4)