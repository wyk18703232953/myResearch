import random


def main(n: int):
    # 生成测试数据：大小为 n x n 的矩阵，包含两个 'B'
    m = n
    grid = [['W' for _ in range(m)] for _ in range(n)]

    # 随机生成两个不同的位置放置 'B'
    x1 = random.randint(0, n - 1)
    y1 = random.randint(0, m - 1)
    while True:
        x2 = random.randint(0, n - 1)
        y2 = random.randint(0, m - 1)
        if x2 != x1 or y2 != y1:
            break

    grid[x1][y1] = 'B'
    grid[x2][y2] = 'B'

    # 将二维数组转换为字符串列表，模拟原始输入 l
    l = [''.join(row) for row in grid]

    # 原始逻辑开始
    x1_found = 0
    x2_found = 0
    y1_found = 0
    y2_found = 0

    for i in range(n):
        for j in range(m):
            if l[i][j] == 'B':
                if x1_found == 0 and y1_found == 0:
                    x1_found, y1_found = [i + 1, j + 1]
                else:
                    x2_found, y2_found = [i + 1, j + 1]

    res = []
    x = 0
    y = 0
    if x2_found != 0:
        x = (x2_found - x1_found) // 2
        y = (y2_found - y1_found) // 2
    res.append(x1_found + x)
    res.append(y1_found + y)
    print(*res)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)