def main(n):
    # Generate deterministic input data based on n
    # Here n is the length of the list 'a'
    a = [((i * 2 + 3) % 5) + 1 for i in range(n)]

    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = a[i]

    for leng in range(2, n + 1):
        for l in range(n + 1):
            if l + leng > n:
                continue
            r = l + leng
            for mid in range(l + 1, n + 1):
                if dp[l][mid] != -1 and dp[l][mid] == dp[mid][r]:
                    dp[l][r] = dp[l][mid] + 1

    dp2 = [float("inf")] * (n + 1)
    for i in range(n + 1):
        dp2[i] = i
        for j in range(i):
            if dp[j][i] != -1:
                dp2[i] = min(dp2[i], dp2[j] + 1)

    # print(dp2[n])
    pass
if __name__ == "__main__":
    main(10)