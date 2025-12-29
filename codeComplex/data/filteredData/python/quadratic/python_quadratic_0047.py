MOD = 1000000007

def add(a, b):
    a %= MOD
    b %= MOD
    return (a + b) % MOD

def main(n: int) -> int:
    # 生成测试数据：前 n-1 行随机设为 'f' 或 's'，最后一行设为 's'
    # 这里给出一种确定性方式：偶数下标为 'f'，奇数下标为 's'
    statements = []
    for i in range(n):
        if i == n - 1:
            statements.append('s')
        else:
            statements.append('f' if i % 2 == 0 else 's')

    dp = [[0 for _ in range(n)] for _ in range(n)]
    prefix = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = 1
    prefix[0][0] = 1

    j = 1
    while j < n:
        dp[0][j] = 0
        prefix[0][j] = dp[0][j] + prefix[0][j - 1]
        j += 1

    i = 1
    while i < n:
        if statements[i - 1] == 'f':
            j = 1
            while j < n:
                dp[i][0] = 0
                prefix[i][0] = 0
                dp[i][j] = dp[i - 1][j - 1]
                prefix[i][j] = add(prefix[i][j - 1], dp[i][j])
                j += 1
        else:
            j = 0
            while j < n:
                if j == 0:
                    dp[i][j] = prefix[i - 1][n - 1]
                else:
                    dp[i][j] = prefix[i - 1][n - 1] - prefix[i - 1][j - 1]
                prefix[i][j] = add(prefix[i][j - 1], dp[i][j])
                j += 1
        i += 1

    ans = 0
    j = 0
    while j < n:
        ans = add(ans, dp[n - 1][j])
        j += 1

    return ans % MOD

# 示例：直接调用 main(n) 获取结果
# print(main(5))