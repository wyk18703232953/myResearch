def main(n):
    mod = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1

    # 生成长度为 n 的指令序列，由 n 确定性生成
    # 规则：奇数下标为 'f'，偶数下标为 's'
    instructions = ['f' if i % 2 == 1 else 's' for i in range(n)]

    for i in range(n):
        nx = [0] * (n + 1)
        s = instructions[i]
        if s == 'f':
            nx[0] = 0
            for j in range(1, n + 1):
                nx[j] = dp[j - 1] % mod

        else:
            nx[n] = dp[n] % mod
            for j in reversed(range(n)):
                nx[j] = (nx[j + 1] + dp[j]) % mod
        if i != n - 1:
            dp = nx
    # print(sum(dp) % mod)
    pass
if __name__ == "__main__":
    main(10)