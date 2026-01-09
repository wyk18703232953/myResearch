def main(n):
    if n <= 0:
        return 0

    # generate deterministic input array a of length n
    # example pattern: a[i] = (i % 5) + 1
    a = [(i % 5) + 1 for i in range(n)]

    max_size = max(600, n + 2)
    new_a = [[0] * max_size for _ in range(max_size)]
    dp = [[0x7fffffff] * max_size for _ in range(max_size)]

    for i in range(n):
        new_a[i + 1][i + 1] = a[i]
        dp[i + 1][i + 1] = 1

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            dp[i][j] = j - i + 1

    for llen in range(2, n + 1):
        for left in range(1, n - llen + 2):
            right = left + llen - 1
            for middle in range(left, right):
                val = dp[left][middle] + dp[middle + 1][right]
                if val < dp[left][right]:
                    dp[left][right] = val
                if (
                    dp[left][middle] == 1
                    and dp[middle + 1][right] == 1
                    and new_a[left][middle] == new_a[middle + 1][right]
                ):
                    dp[left][right] = 1
                    new_a[left][right] = new_a[left][middle] + 1

    result = dp[1][n]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # example deterministic call
    main(5)