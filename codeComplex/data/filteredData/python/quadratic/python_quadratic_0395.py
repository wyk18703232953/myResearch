import random

def main(n):
    # 随机构造一个 n 行 m 列的矩阵，其中有若干个连续的 'B' 组成矩形
    m = n  # 这里简单设为正方形，可按需调整为其它策略

    # 初始化为全 'W'
    grid = [['W' for _ in range(m)] for _ in range(n)]

    # 随机生成一个非空的 'B' 矩形
    top = random.randint(0, n - 1)
    bottom = random.randint(top, n - 1)
    left = random.randint(0, m - 1)
    right = random.randint(left, m - 1)

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            grid[i][j] = 'B'

    # 原始逻辑：在网格中找到所有 'B' 的最小外接矩形中心
    x1 = -1
    x2 = -1
    y1 = -1
    y2 = -1
    for i in range(n):
        s = ''.join(grid[i])
        for j in range(m):
            if s[j] == 'B':
                if x1 == -1:
                    x1 = j + 1
                x2 = max(x2, j + 1)
                if y1 == -1:
                    y1 = i + 1
                y2 = i + 1

    # 输出中心坐标（使用 1-based 下标）
    print((y1 + y2) // 2, (x1 + x2) // 2)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要更改 n
    main(5)