def main(n):
    MOD = 1000000007
    # 构造长度为 n 的指令序列：前一半为 'f'，后一半为 's'
    cmds = ['f' if i < n // 2 else 's' for i in range(n)]

    dp = [1]
    for c in cmds:
        if c == "f":
            dp.insert(0, 0)

        else:
            for i in range(len(dp) - 2, -1, -1):
                dp[i] = (dp[i] + dp[i + 1]) % MOD
    # print(dp[0])
    pass
if __name__ == "__main__":
    main(10)