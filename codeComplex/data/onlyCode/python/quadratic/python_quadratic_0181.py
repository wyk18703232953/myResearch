n = int(input())
values = list(map(int, input().split()))
queries = int(input())

dp = [[0] * 5009 for i in range(5009)]

for i in range(n):
    dp[0][i] = values[i]

for i in range(1, n): # 0 is already populated
    for j in range(n-i+1):
        top = dp[i-1][j]
        right = dp[i-1][j+1]
        dp[i][j] = top ^ right

for i in range(1, n):
    for j in range(n-i+1):
        top = dp[i-1][j]
        right = dp[i-1][j+1]
        dp[i][j] = max(right, max(dp[i][j], top))

for i in range(queries):
    left, right = map(int, input().split())
    last_row = (right - 1) - (left - 1)
    last_column = (left - 1)
    print(dp[last_row][last_column])
    


