mod = 10**9 + 7

def main(n):
    # 生成确定性的指令序列 l，长度为 n
    # 模式：'f' 和 'x' 交替，保证有分支多样性
    if n <= 0:
        print(0)
        return
    l = [('f' if i % 2 == 0 else 'x') for i in range(n)]

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
    print(dp[1][0])


if __name__ == "__main__":
    # 示例：使用 n = 5 进行一次确定性运行
    main(5)