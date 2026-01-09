def main(n):
    mod = 10**9 + 7
    dp = [[0 for _ in range(n + 5)] for _ in range(n + 5)]

    # 确定性生成原来的 n 行字符串输入：
    # 偶数行用 'f'，奇数行用 's'
    # 保证长度为 n
    prev = "-1"
    for i in range(n):
        if i % 2 == 0:
            p = 'f'

        else:
            p = 's'

        if i == 0:
            dp[i][0] = 1

        else:
            c = 0
            if prev == 'f':
                for j in range(n):
                    dp[i][j + 1] = dp[i - 1][j]

            else:
                for j in range(n, -1, -1):
                    c = (c + dp[i - 1][j]) % mod
                    dp[i][j] = c

        prev = p

    result = sum(dp[n - 1]) % mod
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：以 n = 10 作为规模运行一次
    main(10)