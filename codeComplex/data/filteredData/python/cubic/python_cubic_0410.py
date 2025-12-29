import random

def main(n):
    # 生成规模参数
    # 这里简单设定 m = n，k = 2 * n，按需可调整生成逻辑
    m = n
    k = 2 * n

    # 生成测试数据（边权为 1~10 的随机整数）
    horiz_costs = [[random.randint(1, 10) for _ in range(m - 1)] for _ in range(n)]
    vert_costs = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]

    if k % 2 == 1:
        for _ in range(n):
            print(" ".join(["-1"] * m))
        return

    ans = [[[0] * m for _ in range(n)] for _ in range(k // 2 + 1)]

    def costs(i, j, time):
        r = []
        if j < m - 1:
            r.append(2 * horiz_costs[i][j] + ans[time - 1][i][j + 1])
        if j > 0:
            r.append(2 * horiz_costs[i][j - 1] + ans[time - 1][i][j - 1])
        if i < n - 1:
            r.append(2 * vert_costs[i][j] + ans[time - 1][i + 1][j])
        if i > 0:
            r.append(2 * vert_costs[i - 1][j] + ans[time - 1][i - 1][j])
        return r

    for time in range(1, k // 2 + 1):
        for i in range(n):
            for j in range(m):
                best = None
                for c in costs(i, j, time):
                    if best is None or c < best:
                        best = c
                ans[time][i][j] = best if best is not None else 0

    for i in range(n):
        print(" ".join(str(s) for s in ans[-1][i]))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)