def main(n):
    # 映射输入规模 n 到原程序的 n, m, k
    # 这里设定为：网格为 n x n，k = 2 * n（保证为偶数）
    # 若 n < 1，则视为最小规模 1
    if n < 1:
        n = 1
    grid_n = n
    grid_m = n
    k = 2 * n

    inf = 1 << 30

    # 确定性生成 left 矩阵 (grid_n x grid_m-1)
    # left[i][j] = (i + j + 1)
    left = [[i + j + 1 for j in range(grid_m - 1)] for i in range(grid_n)]

    # 确定性生成 down 矩阵 (grid_n-1 x grid_m)
    # down[i][j] = (i * 2 + j + 1)
    if grid_n >= 2:
        down = [[i * 2 + j + 1 for j in range(grid_m)] for i in range(grid_n - 1)]

    else:
        down = []

    # 原逻辑：如果 k 为奇数，输出全 -1
    if k & 1:
        for _ in range(grid_n):
            # print(*([-1] * grid_m))
            pass
        return

    ans = [[0] * grid_m for _ in range(grid_n)]
    half = k // 2
    for _step in range(1, half + 1):
        tmp = [[inf] * grid_m for _ in range(grid_n)]
        for i in range(grid_n):
            for j in range(grid_m):
                if i:
                    tmp[i][j] = min(tmp[i][j], ans[i - 1][j] + down[i - 1][j])
                if i < grid_n - 1:
                    tmp[i][j] = min(tmp[i][j], ans[i + 1][j] + down[i][j])
                if j:
                    tmp[i][j] = min(tmp[i][j], ans[i][j - 1] + left[i][j - 1])
                if j < grid_m - 1:
                    tmp[i][j] = min(tmp[i][j], ans[i][j + 1] + left[i][j])
        ans = tmp

    for i in range(grid_n):
        for j in range(grid_m):
            # print(ans[i][j] * 2, end=' ')
            pass
        # print()
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行规模化实验
    main(5)