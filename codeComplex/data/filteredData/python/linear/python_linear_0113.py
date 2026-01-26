def main(n):
    if n < 1:
        return 0
    if n > 100:
        n = 100
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 101):
        dp[i] = dp[i - 2] + i
    return dp[n]


if __name__ == "__main__":
    # 示例：使用 n=10 作为输入规模
    result = main(10)
    # print(result)
    pass