MOD = int(1e9 + 7)

def main(n):
    if n <= 1:
        # print(1)
        pass
        return

    # 确定性生成长度为 n 的字符串 a，由 'f' 和 's' 组成
    # 模式：索引偶数为 'f'，奇数为 's'
    a = "".join('f' if i % 2 == 0 else 's' for i in range(n))

    dp, s = [], []
    for i in range(n + 1):
        dp.append([0] * (n + 1))
        s.append([0] * (n + 1))

    dp[0][0] = 1
    s[0][0] = 1

    for i in range(1, n):
        for j in range(0, n):
            if a[i - 1] == 'f':
                dp[i][j + 1] = dp[i - 1][j] % MOD
            elif a[i - 1] == 's':
                dp[i][j] = s[i - 1][j] % MOD

        for j in reversed(range(n)):
            s[i][j] = (s[i][j] + dp[i][j] + s[i][j + 1]) % MOD

    # print(s[n - 1][0] % MOD)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 以做规模实验
    main(5)