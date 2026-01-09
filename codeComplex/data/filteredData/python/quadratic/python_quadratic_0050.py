def main(n):
    MOD = 1000000007
    dp = [1]

    # 生成长度为 n 的确定性指令序列：
    # 偶数位置为 "f"，奇数位置为 "s"
    commands = ["f" if i % 2 == 0 else "s" for i in range(n)]

    for c in commands:
        if c == "f":
            dp.insert(0, 0)

        else:
            for i in range(len(dp) - 2, -1, -1):
                dp[i] = (dp[i] + dp[i + 1]) % MOD
    # print(dp[0])
    pass
if __name__ == "__main__":
    main(10)