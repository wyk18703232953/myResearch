MOD = int(1e9 + 7)

def main(n):
    # 生成测试数据：长度为 n 的指令串，由 'f' 和 's' 组成
    # 这里简单生成：前一半为 'f'，后一半为 's'
    half = n // 2
    a = 'f' * half + 's' * (n - half)

    dp, s = [], []
    for _ in range(n + 1):
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

    ans = s[n - 1][0] % MOD
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)