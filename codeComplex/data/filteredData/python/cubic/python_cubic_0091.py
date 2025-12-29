import random

def main(n):
    N = 520
    K = 12
    C = 100 * 1000 + 11

    # 规模 n: 用来生成测试数据
    # 约束：dp 的维度依赖 n 和 K，保持原逻辑 j 最大为 n * K
    k = min(K, max(1, n // 10))  # 示例：k 随 n 变化但不超过原 K

    # 初始化计数数组
    c = [0 for _ in range(C)]
    f = [0 for _ in range(C)]

    # 生成测试数据 a, b, h
    # a, b 长度为 n，值域在 [0, C-1]
    random.seed(0)
    a = [random.randint(0, C - 1) for _ in range(n)]
    b = [random.randint(0, C - 1) for _ in range(n)]

    # h 长度为 k，其中 h[0] 固定为 0，后面 k 个随机
    h = [0] + [random.randint(0, 10) for _ in range(k)]

    for x in a:
        c[x] += 1

    for x in b:
        f[x] += 1

    # dp 尺寸：原程序 i 维最大为 n，j 维最大为 n*k
    dp = [[0 for _ in range(k * n + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n * k + 1):
            if dp[i][j] == 0 and not (i == 0 and j == 0):
                # 可选的小优化：如果 dp[i][j] 为 0 且不是起点，且所有 h[cur] >= 0，则继续
                # 但这里保持原逻辑不剪枝
                pass
            for cur in range(k + 1):
                if j + cur <= n * k:
                    dp[i + 1][j + cur] = max(dp[i + 1][j + cur], dp[i][j] + h[cur])

    ans = 0
    for i in range(C):
        if f[i] != 0:
            if f[i] <= n and c[i] <= n * k:
                ans += dp[f[i]][c[i]]

    return ans


if __name__ == "__main__":
    # 例如用 n = 100 运行
    print(main(100))