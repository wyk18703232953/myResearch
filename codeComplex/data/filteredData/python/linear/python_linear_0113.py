def main(n):
    if n < 1:
        # print(0)
        pass
        return
    if n > 100:
        n = 100
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 101):
        dp[i] = dp[i - 2] + i
    # print(dp[n])
    pass
if __name__ == "__main__":
    main(50)