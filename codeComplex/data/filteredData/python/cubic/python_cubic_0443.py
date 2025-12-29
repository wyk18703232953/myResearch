import random

def main(n):
    # 生成规模参数
    # 为了保持原逻辑完整，这里除了 n 以外，还需要生成 m 和 k1
    # 你可以根据需要修改 m、k1 的生成规则
    m = n  # 示例：令 m = n
    # k1 需要在 [1, 20] 范围内，否则 dp 中不会被正确填充
    k1 = random.randint(1, 20)

    # 生成测试数据：
    # arr: n x m
    # brr: (n - 1) x m
    # 为保证非负且简单，使用小整数
    arr = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
    if n > 1:
        brr = [[random.randint(1, 10) for _ in range(m)] for _ in range(n - 1)]
    else:
        # 当 n == 1 时，brr 实际不会被使用（没有上下移动），但需要占位
        brr = []

    # DP 初始化
    dp = [[[0 for _ in range(21)] for _ in range(m)] for _ in range(n)]

    for k in range(1, 21):
        for i in range(n):
            for j in range(m):
                if k % 2 == 1:
                    dp[i][j][k] = -1
                else:
                    val = 10 ** 9
                    if i > 0:
                        val = min(val, dp[i - 1][j][k - 2] + brr[i - 1][j] * 2)
                    if i < n - 1:
                        val = min(val, dp[i + 1][j][k - 2] + brr[i][j] * 2)
                    if j > 0:
                        val = min(val, dp[i][j - 1][k - 2] + arr[i][j - 1] * 2)
                    if j < m - 1:
                        val = min(val, dp[i][j + 1][k - 2] + arr[i][j] * 2)
                    dp[i][j][k] = val

    # 输出结果（与原程序一致）
    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(dp[i][j][k1]))
        print(" ".join(row))


if __name__ == "__main__":
    # 示例调用：可以在此处修改 n 以测试
    main(4)