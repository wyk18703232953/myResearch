mod = 10**9 + 7

def main(n: int) -> int:
    # 生成测试数据：长度为 n 的字符串数组，只含 'f' 或 's'
    # 这里简单生成交替模式：'f','s','f','s',...
    l = [('f' if i % 2 == 0 else 's') for i in range(n)]

    dp = [[0] * (n + 2) for _ in range(n + 1)]
    for i in range(n + 2):
        dp[n][i] = 1

    for i in range(n - 1, 0, -1):
        s = 0
        for j in range(n + 1):
            s += dp[i + 1][j]
            s %= mod
            if l[i - 1] == 'f':
                dp[i][j] = dp[i + 1][j + 1]

            else:
                dp[i][j] = s

    return dp[1][0]


if __name__ == "__main__":
    # 示例调用：可自行修改 n 测试
    n = 5
    # print(main(n))
    pass