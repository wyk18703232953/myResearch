import random

def main(n: int):
    # 1. 根据 n 生成测试数据
    # 这里将 r, g, b 都设为 n，颜色值为 1..n 的随机排列
    # 如果希望不同规模，可自行调整 r, g, b 与 n 的关系
    r = g = b = max(1, min(n, 200))  # 保证不超过 dp 维度 200 且至少为 1

    rs = [random.randint(1, 1000) for _ in range(r)]
    gs = [random.randint(1, 1000) for _ in range(g)]
    bs = [random.randint(1, 1000) for _ in range(b)]

    # 2. 保持原始逻辑
    rs.sort()
    gs.sort()
    bs.sort()
    rs.reverse()
    gs.reverse()
    bs.reverse()

    # dp 的最大维度在原代码中固定为 201
    dp = [[[0] * 201 for _ in range(201)] for _ in range(201)]

    max_i = min(r, g)
    max_j = min(g, b)
    max_k = min(b, r)

    for i in range(max_i + 1):
        for j in range(max_j + 1):
            for k in range(max_k + 1):
                options = []
                # 对应原代码中的三种转移
                if i != 0:
                    if i + k - 1 < r and i + j - 1 < g:
                        options.append(dp[i - 1][j][k] + rs[i + k - 1] * gs[i + j - 1])
                    else:
                        options.append(dp[i - 1][j][k])
                if j != 0:
                    if i + j - 1 < g and j + k - 1 < b:
                        options.append(dp[i][j - 1][k] + gs[i + j - 1] * bs[j + k - 1])
                    else:
                        options.append(dp[i][j - 1][k])
                if k != 0:
                    if j + k - 1 < b and i + k - 1 < r:
                        options.append(dp[i][j][k - 1] + bs[j + k - 1] * rs[i + k - 1])
                    else:
                        options.append(dp[i][j][k - 1])

                if options:
                    dp[i][j][k] = max(options)

    result = dp[max_i][max_j][max_k]
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)