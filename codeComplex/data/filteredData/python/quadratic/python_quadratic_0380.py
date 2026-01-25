def main(n):
    # 映射关系：n -> 正方形网格 n x n
    # 生成一个 n x n 的字符网格，初始全部为 'W'
    # 在其中放置一个从 (n//4, n//4) 到 (n//2, n//2) 的 'B' 矩形块（若 n 较小时自动收缩）
    if n <= 0:
        return

    m = n
    grid = [['W' for _ in range(m)] for _ in range(n)]

    # 决定 B 区域的边界（确保在范围内且至少有一个 B）
    bx1 = n // 4
    by1 = n // 4
    bx2 = max(bx1, n // 2)
    by2 = max(by1, n // 2)
    bx1 = min(bx1, n - 1)
    by1 = min(by1, m - 1)
    bx2 = min(bx2, n - 1)
    by2 = min(by2, m - 1)

    for i in range(bx1, bx2 + 1):
        for j in range(by1, by2 + 1):
            grid[i][j] = 'B'

    l = ["".join(row) for row in grid]

    # 以下是原始算法逻辑
    minX, minY, maxX, maxY = n, m, 0, 0
    for i in range(n):
        for j in range(m):
            if l[i][j] == 'B':
                minX = min(minX, i)
                minY = min(minY, j)
                maxX = max(maxX, i)
                maxY = max(maxY, j)
    print((minX + maxX) // 2 + 1, (minY + maxY) // 2 + 1)


if __name__ == "__main__":
    # 示例调用，可按需修改 n 来做规模实验
    main(10)