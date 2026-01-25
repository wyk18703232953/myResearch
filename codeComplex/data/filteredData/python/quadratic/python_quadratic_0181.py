def main(n):
    # Interpret n as both the length of values and the number of queries
    if n <= 0:
        return

    # Deterministic generation of input data
    # values: a length-n list of integers
    values = [(i * 3 + 1) ^ (i // 2) for i in range(n)]

    # queries: n intervals [left, right] within [1, n]
    # Constructed so that 1 <= left <= right <= n and covers varying lengths
    queries = []
    for i in range(n):
        left = (i % n) + 1
        right = n - (i % (n - i if n - i > 0 else 1))
        if right < left:
            right = left
        queries.append((left, right))

    max_n = n if n <= 5009 else 5009
    dp = [[0] * 5009 for _ in range(5009)]

    # Populate first row with values (truncate if n > 5009)
    for i in range(max_n):
        dp[0][i] = values[i]

    # First DP phase
    for i in range(1, max_n):
        for j in range(max_n - i + 1):
            top = dp[i - 1][j]
            right = dp[i - 1][j + 1]
            dp[i][j] = top ^ right

    # Second DP phase
    for i in range(1, max_n):
        for j in range(max_n - i + 1):
            top = dp[i - 1][j]
            right = dp[i - 1][j + 1]
            dp[i][j] = max(right, max(dp[i][j], top))

    # Process queries (truncate to max_n if needed)
    q = n if n <= 5009 else 5009
    for i in range(q):
        left, right = queries[i]
        # Clamp query bounds to [1, max_n]
        if left < 1:
            left = 1
        if right > max_n:
            right = max_n
        if right < left:
            right = left
        last_row = (right - 1) - (left - 1)
        last_column = (left - 1)
        if last_row < 0 or last_row >= max_n or last_column < 0 or last_column >= 5009:
            print(0)
        else:
            print(dp[last_row][last_column])


if __name__ == "__main__":
    main(1000)