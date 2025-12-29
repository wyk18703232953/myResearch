import random

def main(n):
    # 这里将规模参数 n 用作行数，列数 m 与 n 相同，也可按需调整
    m = n
    # 为了可重复性，可以固定随机种子
    random.seed(0)

    # 生成测试数据：
    # k：偶数（若为奇数，原逻辑直接输出 -1）
    # 这里令 k 在 [2, 2*n] 内的偶数
    if n > 0:
        k = random.randrange(1, n + 1) * 2
    else:
        k = 2

    # hor: n 行，每行 m-1 个非负整数
    hor = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    # ver: n-1 行，每行 m 个非负整数
    ver = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

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

    grid = [[0] * m for _ in range(n)]
    if k % 2:
        for _ in range(n):
            print(" ".join(["-1"] * m))
    else:
        for _ in range(k // 2):
            new_grid = [[roll(i, j) for j in range(m)] for i in range(n)]
            grid = new_grid[:]
        for i in range(n):
            print(" ".join(map(str, grid[i])))


if __name__ == "__main__":
    # 示例：调用 main(4)
    main(4)