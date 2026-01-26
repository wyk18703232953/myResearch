def main(n):
    # Map n to sizes of the three arrays
    # Make them balanced and O(n) total size
    r = n
    g = n
    b = n

    # Deterministic data generation
    l1 = [(i * 2 + 1) % 1000 for i in range(r)]
    l2 = [(i * 3 + 2) % 1000 for i in range(g)]
    l3 = [(i * 5 + 3) % 1000 for i in range(b)]

    l1.sort(reverse=True)
    l2.sort(reverse=True)
    l3.sort(reverse=True)

    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    ans = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i > 0 and j > 0 and k > 0:
                    dp[i][j][k] = max(
                        l1[i - 1] * l2[j - 1] + dp[i - 1][j - 1][k],
                        l1[i - 1] * l3[k - 1] + dp[i - 1][j][k - 1],
                        l2[j - 1] * l3[k - 1] + dp[i][j - 1][k - 1],
                    )

                else:
                    if i > 0 and j > 0:
                        dp[i][j][k] = max(dp[i][j][k], l1[i - 1] * l2[j - 1] + dp[i - 1][j - 1][k])
                    if i > 0 and k > 0:
                        dp[i][j][k] = max(dp[i][j][k], l1[i - 1] * l3[k - 1] + dp[i - 1][j][k - 1])
                    if j > 0 and k > 0:
                        dp[i][j][k] = max(dp[i][j][k], l2[j - 1] * l3[k - 1] + dp[i][j - 1][k - 1])

                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]

    # print(ans)
    pass
if __name__ == "__main__":
    main(5)