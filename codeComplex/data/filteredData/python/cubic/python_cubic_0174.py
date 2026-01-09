def main(n):
    if n <= 0:
        return 0
    a = [i % 5 for i in range(n)]
    rows, cols = (n + 1, n + 1)
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]
    for i in range(n):
        dp[i][i] = a[i]
    for last in range(1, n):
        for first in range(last - 1, -1, -1):
            for mid in range(last, first, -1):
                if dp[first][mid - 1] != -1 and dp[mid][last] != -1 and dp[first][mid - 1] == dp[mid][last]:
                    dp[first][last] = dp[first][mid - 1] + 1
    ans = [i + 1 for i in range(n)]
    for i in range(n):
        for j in range(i, -1, -1):
            if j - 1 >= 0:
                if dp[j][i] != -1:
                    ans[i] = min(ans[i], ans[j - 1] + 1)
            elif dp[0][i] != -1:
                ans[i] = 1
    return ans[n - 1]


if __name__ == "__main__":
    # print(main(10))
    pass