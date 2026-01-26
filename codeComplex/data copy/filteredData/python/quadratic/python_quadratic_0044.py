def main(n):
    MOD = 1000000007
    # Deterministically generate input structure:
    # First "line" is integer n (scale)
    # Then n commands, each either "f" or "s"
    # Use a simple periodic pattern depending on n
    cmds = [("f" if (i % 3 == 0) else "s") for i in range(n)]

    dp = [1]
    for c in cmds:
        if c == "f":
            dp.insert(0, 0)

        else:
            for i in range(len(dp) - 2, -1, -1):
                dp[i] = (dp[i] + dp[i + 1]) % MOD
    # print(dp[0])
    pass
if __name__ == "__main__":
    main(10)