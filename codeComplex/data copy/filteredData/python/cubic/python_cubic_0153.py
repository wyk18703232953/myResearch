def main(n):
    # Generate deterministic test data based on n
    # Original code expects:
    # n : length of array
    # arr : list of n integers
    # We generate arr[i] = (i % 5) + 1 to keep values small but deterministic
    arr = [(i % 5) + 1 for i in range(n)]

    # dp is fixed size 500x500 in original code
    max_size = 500
    if n > max_size:
        n = max_size
        arr = arr[:n]

    dp = [[0 for _ in range(max_size)] for _ in range(max_size)]
    dp2 = [0 for _ in range(max_size + 1)]

    for i in range(n):
        dp[i][i] = arr[i]

    i = n - 2
    while ~i:
        j = i + 1
        while j < n:
            dp[i][j] = -1
            for k in range(i, j):
                if (~dp[i][k] and dp[i][k]) == dp[k + 1][j]:
                    dp[i][j] = dp[i][k] + 1
            j += 1
        i -= 1

    for i in range(1, n + 1):
        dp2[i] = 10**9
        for j in range(i):
            if ~dp[j][i - 1]:
                dp2[i] = min(dp2[i], dp2[j] + 1)

    # print(dp2[n])
    pass
if __name__ == "__main__":
    main(10)