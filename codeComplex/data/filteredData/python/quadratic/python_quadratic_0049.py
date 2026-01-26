def main(n):
    MOD = 1000000007
    dp = [1]
    for IND in range(n):
        # deterministically generate c based on IND
        # pattern: first half "f", second half "s"
        if IND < n // 2:
            c = "f"

        else:
            c = "s"
        if c == "f":
            dp.insert(0, 0)

        else:
            for i in range(len(dp) - 2, -1, -1):
                dp[i] = (dp[i] + dp[i + 1]) % MOD
    # print(dp[0])
    pass
if __name__ == "__main__":
    main(10)