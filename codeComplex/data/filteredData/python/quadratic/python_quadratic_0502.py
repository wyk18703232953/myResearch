def isValid(field, y, x):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if field[y + i][x + j] == '.':
                return False
    return True


def fill(cur, y, x):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            cur[y + i][x + j] = '#'


def generate_test_data(n):
    # 生成一个 n x n 的 sig：
    # 先全部填充为 '.'，再在中间区域铺几块符合规则的 3x3 图案
    sig = [['.' for _ in range(n)] for _ in range(n)]

    # 简单策略：每隔 3 行 3 列放一个图案，保证边界合法
    for i in range(0, n - 2, 3):
        for j in range(0, n - 2, 3):
            # 填一个合法的 3x3：除中心之外都为 '#'
            for dy in range(3):
                for dx in range(3):
                    if dy == 1 and dx == 1:
                        continue
                    sig[i + dy][j + dx] = '#'
            # 中心点可以随意，这里设为 '.'
            sig[i + 1][j + 1] = '.'

    return sig


def main(n):
    # 根据 n 生成测试数据（这里令 m = n，生成 n x n 的矩阵）
    sig = generate_test_data(n)
    n_rows = len(sig)
    m_cols = len(sig[0]) if n_rows > 0 else 0

    # 初始化 cur 为全 '.'
    cur = [['.' for _ in range(m_cols)] for _ in range(n_rows)]

    # 按原逻辑填充
    for i in range(n_rows - 2):
        for j in range(m_cols - 2):
            if isValid(sig, i, j):
                fill(cur, i, j)

    # 判断并输出
    if sig == cur:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用：可以修改这里的规模 n 来测试
    main(9)