def color8(i, j, op, n, m):
    # 给 op 中的 3x3 区域涂成特定的 # 形状
    if i > n - 3 or j > m - 3:
        return
    op[i][j] = '#'
    op[i][j + 1] = '#'
    op[i][j + 2] = '#'
    op[i + 1][j] = '#'
    op[i + 1][j + 2] = '#'
    op[i + 2][j] = '#'
    op[i + 2][j + 1] = '#'
    op[i + 2][j + 2] = '#'


def check_grid(ip):
    # 核心逻辑：判断 ip 是否能由若干 color8 图案叠加得到
    n = len(ip)
    m = len(ip[0]) if n > 0 else 0
    op = [['.' for _ in range(m)] for _ in range(n)]
    b = 0

    for i in range(n):
        for j in range(m):
            if ip[i][j] == '#':
                # 尝试在 (i, j) 放置一个 3x3 图案
                if i + 2 < n and j + 2 < m and ip[i + 2][j + 2] == '#':
                    temp = (
                        ip[i][j] == '#' and
                        ip[i][j + 1] == '#' and
                        ip[i][j + 2] == '#' and
                        ip[i + 1][j] == '#' and
                        ip[i + 1][j + 2] == '#' and
                        ip[i + 2][j] == '#' and
                        ip[i + 2][j + 1] == '#' and
                        ip[i + 2][j + 2] == '#'
                    )
                    if temp:
                        color8(i, j, op, n, m)

    for i in range(n):
        if ''.join(op[i]) != ip[i]:
            return "NO"
            b = 1
            break
    if b == 0:
        return "YES"


def generate_test_data(n):
    # 生成一个 n x n 测试网格：
    # 规则：每 4 行、每 4 列的左上角放一个 3x3 的 color8 图案，其余为 '.'
    size = n
    grid = [['.' for _ in range(size)] for _ in range(size)]

    def safe_color8(i, j):
        if i + 2 >= size or j + 2 >= size:
            return
        grid[i][j] = '#'
        grid[i][j + 1] = '#'
        grid[i][j + 2] = '#'
        grid[i + 1][j] = '#'
        grid[i + 1][j + 2] = '#'
        grid[i + 2][j] = '#'
        grid[i + 2][j + 1] = '#'
        grid[i + 2][j + 2] = '#'

    step = 4  # 间隔，避免互相覆盖得太复杂
    for i in range(0, size, step):
        for j in range(0, size, step):
            safe_color8(i, j)

    return [''.join(row) for row in grid]


def main(n):
    # n 为规模，这里用 n 生成 n x n 测试网格，然后跑原逻辑
    ip = generate_test_data(n)
    result = check_grid(ip)
    print(result)


if __name__ == "__main__":
    # 示例：可改为任意正整数规模
    main(7)