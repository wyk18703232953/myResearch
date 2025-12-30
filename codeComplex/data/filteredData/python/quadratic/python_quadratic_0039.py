M = 10**9 + 7

def main(n: int) -> int:
    # 生成测试数据：长度为 n 的指令序列 a，每个元素为 'f' 或 's'
    # 这里简单设定为前半段 'f'，后半段 's'，你可按需要修改生成策略
    a = []
    for i in range(n):
        if i < n // 2:
            a.append('f')
        else:
            a.append('s')

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
    return sum(dp[n - 1]) % M