#!/usr/bin/env python3
import random
from math import inf

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solve(N, M, K, wx, wy):
    if K & 1:
        # K 为奇数时，全为 -1
        res = [[-1 for _ in range(M)] for _ in range(N)]
        return res

    # mem[step][y][x]
    mem = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]

    half = K // 2
    for kk in range(1, half + 1):
        for yy in range(N):
            for xx in range(M):
                best = inf
                for d in range(4):
                    y = yy + dy[d]
                    x = xx + dx[d]
                    if y < 0 or y >= N or x < 0 or x >= M:
                        continue

                    if d == 0:        # 向下：使用 wx[yy][xx]
                        best = min(best, mem[kk - 1][y][x] + wx[yy][xx] * 2)
                    elif d == 1:      # 向右：使用 wy[yy][xx]
                        best = min(best, mem[kk - 1][y][x] + wy[yy][xx] * 2)
                    elif d == 2:      # 向上：使用 wx[yy][x]
                        best = min(best, mem[kk - 1][y][x] + wx[yy][x] * 2)
                    else:             # 向左：使用 wy[y][xx]
                        best = min(best, mem[kk - 1][y][x] + wy[y][xx] * 2)
                mem[kk][yy][xx] = best

    res = [[mem[half][yy][xx] for xx in range(M)] for yy in range(N)]
    return res


def main(n):
    """
    n 为规模参数：
    - 这里简单设置 N = M = n，K = 2 * n（保证为偶数）
    - 边权随机生成在 [1, 10] 范围内
    """
    N = n
    M = n
    K = 2 * n if 2 * n > 0 else 2  # 保证 K >= 2 且为偶数

    # 生成测试数据
    random.seed(0)
    wx = [[random.randint(1, 10) for _ in range(M)] for _ in range(N)]
    wy = [[random.randint(1, 10) for _ in range(M)] for _ in range(N - 1)]

    ans = solve(N, M, K, wx, wy)

    # 输出结果，与原程序格式一致
    for yy in range(N):
        print(" ".join(str(ans[yy][xx]) for xx in range(M)))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)