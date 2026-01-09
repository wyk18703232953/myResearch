def main(n):
    # Generate deterministic test data based on n
    # Interpret n as the length of arrays a and b
    # a: strictly increasing sequence 1..n
    a = [i + 1 for i in range(n)]
    # b: some deterministic pattern, e.g., i % 7 + 1
    b = [i % 7 + 1 for i in range(n)]

    PI = float('inf')
    ans = PI
    dp = [[PI for _ in range(4)] for _ in range(n)]

    for i in range(n):
        dp[i][1] = b[i]
        for j in range(i):
            if a[j] < a[i]:
                dp[i][2] = min(dp[i][2], dp[j][1] + b[i])
                dp[i][3] = min(dp[i][3], dp[j][2] + b[i])
                ans = min(ans, dp[i][3])

    result = ans if ans != PI else -1
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example call for time complexity experiment
    main(1000)