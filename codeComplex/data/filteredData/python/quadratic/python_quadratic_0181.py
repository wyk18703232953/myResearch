def main(n):
    # Interpret n as the length of the values array and also the number of queries
    size = n
    if size <= 0:
        return

    # Deterministically generate values of length n
    values = [(i * 3 + 7) % 100000 for i in range(size)]

    queries = size

    # dp is fixed-size 5009x5009 in the original code
    MAXN = 5009
    dp = [[0] * MAXN for _ in range(MAXN)]

    # Initialize first row with values
    for i in range(size):
        dp[0][i] = values[i]

    # First DP: XOR triangle
    for i in range(1, size):  # 0 is already populated
        limit = size - i + 1
        for j in range(limit):
            top = dp[i - 1][j]
            right = dp[i - 1][j + 1]
            dp[i][j] = top ^ right

    # Second DP: range maximum propagation
    for i in range(1, size):
        limit = size - i + 1
        for j in range(limit):
            top = dp[i - 1][j]
            right = dp[i - 1][j + 1]
            current = dp[i][j]
            dp[i][j] = max(right, current, top)

    # Deterministically generate queries.
    # Original queries are 1-based [left, right] with 1 <= left <= right <= n
    # We create 'queries' pairs covering various ranges.
    for idx in range(queries):
        # Spread left over 1..n
        left = (idx % size) + 1
        # Ensure right >= left and within [1, n]
        right = left + (idx // 2) % (size - left + 1)
        last_row = (right - 1) - (left - 1)
        last_column = (left - 1)
        # print(dp[last_row][last_column])
        pass
if __name__ == "__main__":
    # Example call; adjust n for different input scales
    main(1000)