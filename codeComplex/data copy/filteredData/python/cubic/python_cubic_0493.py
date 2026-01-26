from math import inf

def main(n):
    # 映射输入规模 n 到原程序中的 n, m, k
    # 这里设定一个可扩展映射：网格为 n x n，k 与 n 挂钩保证多次迭代
    original_n = max(1, n)
    original_m = max(1, n)
    # 令 k 为一个偶数，与 n 线性相关，保证存在非 -1 的路径计算
    k = 2 * max(1, n // 2)

    n_rows = original_n
    m_cols = original_m

    # 构造 horizontal: n x (m-1)
    # 定义为 (i + j + 1)，保证正权且随规模线性增长
    horizontal = []
    for i in range(n_rows):
        row = [(i + j + 1) for j in range(m_cols - 1)]
        horizontal.append(row)

    # 构造 vertical: (n-1) x m
    # 定义为 (i + j + 2)，与 horizontal 区分但同样简单确定
    vertical = []
    for i in range(n_rows - 1):
        row = [(i + j + 2) for j in range(m_cols)]
        vertical.append(row)

    n_local = n_rows
    m_local = m_cols

    if k & 1:
        ans = ["-1"] * m_local
        for _ in range(n_local):
            # print(*ans)
            pass

    else:
        grid = [[0 for _ in range(m_local)] for _ in range(n_local)]
        for _ in range(k // 2):
            X = [[inf for _ in range(m_local)] for _ in range(n_local)]
            for i in range(n_local):
                for j in range(m_local):
                    if i >= 1:
                        X[i][j] = min(2 * vertical[i - 1][j] + grid[i - 1][j], X[i][j])
                    if i < n_local - 1:
                        X[i][j] = min(2 * vertical[i][j] + grid[i + 1][j], X[i][j])
                    if j >= 1:
                        X[i][j] = min(2 * horizontal[i][j - 1] + grid[i][j - 1], X[i][j])
                    if j < m_local - 1:
                        X[i][j] = min(2 * horizontal[i][j] + grid[i][j + 1], X[i][j])
            grid = [row[:] for row in X]
        for i in range(n_local):
            # print(*grid[i])
            pass
if __name__ == "__main__":
    main(5)