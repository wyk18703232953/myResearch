from random import randint


def main(n: int):
    # 1. 根据规模 n 生成测试数据
    # 为了形成有意义的三维 DP，将 r,g,b 控制在 1..n 范围内
    r = max(1, n // 3)
    g = max(1, n // 3)
    b = max(1, n - r - g)
    # 若 n 太小（例如 n=1、2），保证 r,g,b 至少为 1
    if r == 0:
        r = 1
    if g == 0:
        g = 1
    if b == 0:
        b = 1

    # 生成随机数组，值范围可根据需要调整
    rs = [randint(1, 10) for _ in range(r)]
    gs = [randint(1, 10) for _ in range(g)]
    bs = [randint(1, 10) for _ in range(b)]

    rs.sort()
    gs.sort()
    bs.sort()

    # 2. 原逻辑：三维 DP
    ans = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(1, r + 1):
        for j in range(1, g + 1):
            ans[i][j][0] = ans[i - 1][j - 1][0] + rs[i - 1] * gs[j - 1]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(1, b + 1):
                new_len = bs[k - 1]

                if i == 0:
                    i_len = 0
                else:
                    i_len = ans[i - 1][j][k - 1] + rs[i - 1] * new_len

                if j == 0:
                    j_len = 0
                else:
                    j_len = ans[i][j - 1][k - 1] + gs[j - 1] * new_len

                if i > 0 and j > 0:
                    i_j_len = ans[i - 1][j - 1][k] + rs[i - 1] * gs[j - 1]
                else:
                    i_j_len = 0

                ans[i][j][k] = max(
                    i_len,
                    j_len,
                    ans[i][j][k - 1],
                    i_j_len
                )

    # 输出最终结果（原程序只输出 ans[r][g][b]）
    print(ans[r][g][b])


if __name__ == "__main__":
    # 示例：可修改为任意规模
    main(9)