M = 10**9 + 7

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    # 生成确定性的指令序列 a：长度为 n，每个元素为 'f' 或 's'
    # 规则：i % 2 == 0 -> 'f'，否则 's'
    a = ['f' if i % 2 == 0 else 's' for i in range(n)]
    dp = [[0] * (n + 5) for _ in range(n + 2)]
    dp[0][0] = 1
    for i in range(1, n):
        count = 0
        if a[i - 1] == 'f':
            for j in range(n - 2, -1, -1):
                if dp[i - 1][j] > 0:
                    dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % M

        else:
            for j in range(n - 2, -1, -1):
                if dp[i - 1][j] > 0:
                    count = (count + dp[i - 1][j]) % M
                dp[i][j] = (dp[i][j] + count) % M
    # print(sum(dp[n - 1]) % M)
    pass
if __name__ == "__main__":
    main(5)