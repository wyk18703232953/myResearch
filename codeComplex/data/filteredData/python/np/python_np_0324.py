# 0 denotes white white
# 1 denotes white black
# 2 denotes black white
# 3 denotes black black

pri = 998244353

def main(n: int):
    # 生成测试数据：根据规模 n 构造一个合法的 k
    # 原程序中 k 最大为 2*n，因此这里取 k = 2*n（也可以按需修改策略）
    k = 2 * n
    if n == 0:
        # print(0)
        pass
        return
    if k > 2000:
        # 原程序的数组第三维大小为 2001（下标 0..2000），保证不越界
        k = 2000

    # dp[i][j][t] 在原代码中含义略有混乱，这里保持与原代码的维度一致：
    # dp[2][1001][2001]
    dp = [[[0 for _ in range(2001)] for _ in range(1001)] for _ in range(2)]

    # 原代码逻辑
    for i in range(1, n + 1):
        if i == 1:
            dp[0][i][1] = 2
            dp[1][i][2] = 2
            continue
        for j in range(1, (2 * i) + 1):
            # 这里按照原代码使用，注意下标可能越界时要判断
            v0 = dp[0][i - 1][j]
            v0_prev = dp[0][i - 1][j - 1] if j - 1 >= 0 else 0
            v1 = dp[1][i - 1][j]
            v1_prev2 = dp[1][i - 1][j - 2] if j - 2 >= 0 else 0

            dp[0][i][j] = (v0 + v0_prev + 2 * v1) % pri
            dp[1][i][j] = (2 * v0_prev + v1 + v1_prev2) % pri

    y = (dp[0][n][k] + dp[1][n][k]) % pri
    # print(y)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5) 作为测试，可按需要修改
    main(5)