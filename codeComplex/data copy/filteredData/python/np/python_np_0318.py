MOD = 998244353

def main(n):
    # 根据 n 生成测试数据：
    # 这里令 k = n（可按需要调整生成规则）
    k = n

    # 若 k 太小，需避免访问负索引
    if k < 1:
        # print(0)
        pass
        return

    # dp[2][k+2][4]
    dp = [[[0 for _ in range(4)] for _ in range(k + 2)] for _ in range(2)]
    if k >= 2:
        dp[1][2][0] = 1
        dp[1][2][1] = 1
    dp[1][1][2] = 1
    dp[1][1][3] = 1

    for n1 in range(1, n):
        for k1 in range(1, k + 1):
            # 拷贝上一层
            dp[0][k1][0] = dp[1][k1][0]
            dp[0][k1][1] = dp[1][k1][1]
            dp[0][k1][2] = dp[1][k1][2]
            dp[0][k1][3] = dp[1][k1][3]

        for k1 in range(1, k + 1):
            dp00 = dp[0][k1][0]
            dp01 = dp[0][k1][1]
            dp02 = dp[0][k1][2]
            dp03 = dp[0][k1][3]

            val_k1_2_0 = dp[0][k1 - 2][1] if k1 - 2 >= 0 else 0
            val_k1_2_1 = dp[0][k1 - 2][0] if k1 - 2 >= 0 else 0
            val_k1_1_2 = dp[0][k1 - 1][2] if k1 - 1 >= 0 else 0
            val_k1_1_3 = dp[0][k1 - 1][3] if k1 - 1 >= 0 else 0

            dp[1][k1][0] = (dp00 + val_k1_2_0 + val_k1_1_2 + val_k1_1_3) % MOD
            dp[1][k1][1] = (dp01 + val_k1_2_1 + val_k1_1_2 + val_k1_1_3) % MOD
            dp[1][k1][2] = (dp02 + dp01 + dp00 + val_k1_1_3) % MOD
            dp[1][k1][3] = (dp03 + dp01 + dp00 + val_k1_1_2) % MOD

    total = 0
    for i in range(4):
        total = (total + dp[1][k][i]) % MOD

    # print(total % MOD)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)