def main(n):
    # Interpret n as both the array length and k (k <= n and k >= 1)
    if n <= 0:
        return
    k = max(1, n // 2)

    # Deterministic array generation
    arr = [(i * 17 + 23) % 100000 for i in range(n)]

    l = []
    for i in range(n):
        l.append((arr[i], i))

    l.sort(reverse=True)

    dp = []
    x = 0
    for i in range(k):
        dp.append(l[i][1])
        x = x + l[i][0]

    print(x)
    dp.sort()
    dp = [-1] + dp

    length = len(dp)
    for i in range(1, length - 1):
        print(dp[i] - dp[i - 1], end=" ")
    print(n - 1 - dp[length - 2])


if __name__ == "__main__":
    main(10)