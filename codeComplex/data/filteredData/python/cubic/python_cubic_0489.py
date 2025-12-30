import random

def main(n):
    # 生成规模参数
    # 这里令 m = n，k = 2*n（保证为偶数且规模随 n 变化）
    m = n
    k = 2 * n

    # 生成测试数据：hor 为 n x m，ver 为 (n-1) x m
    # 可按需要调整数据范围
    hor = [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]
    ver = [[random.randint(0, 9) for _ in range(m)] for _ in range(n - 1)]

    grid = [[0] * m for _ in range(n)]

    def roll(i, j):
        ways = []
        if j:
            ways.append(2 * hor[i][j - 1] + grid[i][j - 1])
        if m - 1 - j:
            ways.append(2 * hor[i][j] + grid[i][j + 1])
        if i:
            ways.append(2 * ver[i - 1][j] + grid[i - 1][j])
        if n - 1 - i:
            ways.append(2 * ver[i][j] + grid[i + 1][j])
        return min(ways)

    if k % 2:
        for _ in range(n):
            print(" ".join(["-1"] * m))
    else:
        for _ in range(k // 2):
            new_grid = [[roll(i, j) for j in range(m)] for i in range(n)]
            grid = [row[:] for row in new_grid]
        for i in range(n):
            print(" ".join(map(str, grid[i])))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)