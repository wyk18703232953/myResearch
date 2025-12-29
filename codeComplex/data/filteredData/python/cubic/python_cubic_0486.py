import math
import random


def around(x, y, n, m, hor, ver, mtx):
    a, b, c, d = [math.inf] * 4

    if x > 0:
        a = hor[y][x - 1] * 2 + mtx[y][x - 1]

    if x < m - 1:
        b = hor[y][x] * 2 + mtx[y][x + 1]

    if y > 0:
        c = ver[y - 1][x] * 2 + mtx[y - 1][x]

    if y < n - 1:
        d = ver[y][x] * 2 + mtx[y + 1][x]

    return min(a, b, c, d)


def main(n):
    # 这里将 n 作为矩阵的行数规模，
    # 列数 m 与 n 相同，步数 k 也与 n 相关生成。
    m = n
    k = 2 * n  # 保证为偶数，避免原程序中直接输出 -1 的情况

    # 生成测试数据：权重为 1..9 的随机整数
    hor = [[random.randint(1, 9) for _ in range(m - 1)] for _ in range(n)]
    ver = [[random.randint(1, 9) for _ in range(m)] for _ in range(n - 1)]

    if k % 2:
        for _ in range(n):
            print('-1 ' * m)
        return

    _old = [[0] * m for _ in range(n)]
    for _ in range(k // 2):
        _new = [[0] * m for _ in range(n)]

        for x in range(m):
            for y in range(n):
                _new[y][x] = around(x, y, n, m, hor, ver, _old)

        _old = _new

    for row in _old:
        print(*row)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)