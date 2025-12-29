import random

def main(n):
    # 生成测试数据：n, m, k 以及边权矩阵 hor, ver
    # 这里示例设置：m = n，k 为不超过 2n 的偶数
    m = n
    if n <= 0:
        return
    # k 取一个与 2*n 挂钩的偶数（至少为 2）
    k = max(2, (2 * n // 2) * 2)

    # 生成随机边权，范围可按需调整
    max_w = 10
    hor = [[random.randint(1, max_w) for _ in range(m - 1)] for _ in range(n)]
    ver = [[random.randint(1, max_w) for _ in range(m)] for _ in range(n - 1)]

    if k % 2:
        for _ in range(n):
            print('-1 ' * m)
        return

    mtx_old = [[0] * m for _ in range(n)]

    def neighbours(x, y):
        a = 1e18
        b = 1e18
        c = 1e18
        d = 1e18
        if x > 0:
            a = hor[y][x - 1] * 2 + mtx_old[y][x - 1]
        if x < m - 1:
            b = hor[y][x] * 2 + mtx_old[y][x + 1]
        if y > 0:
            c = ver[y - 1][x] * 2 + mtx_old[y - 1][x]
        if y < n - 1:
            d = ver[y][x] * 2 + mtx_old[y + 1][x]
        return min(a, b, c, d)

    for _ in range(k // 2):
        mtx_new = [[0] * m for _ in range(n)]
        for x in range(m):
            for y in range(n):
                mtx_new[y][x] = neighbours(x, y)
        mtx_old = mtx_new

    for row in mtx_old:
        print(*row)


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(4)