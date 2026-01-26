from math import inf


n, m, k = map(int, input().split())
horizontal_costs = []
vertical_costs = []
for _ in range(n):
    horizontal_costs.append(list(map(int, input().split())))
for _ in range(n-1):
    vertical_costs.append(list(map(int, input().split())))

dp = [[[inf] * (k // 2 + 1) for _ in range(m)] for _ in range(n)]

# dp[a][b][c] - smallest cost of moving c squares from (a, b)
# ans[a][b] = 2 * dp[a][b][k//2] if k % 2 == 0 else -1


def find_cost(a, b, c):
    global dp
    if a < 0 or a > n-1 or b < 0 or b > m-1:
        return inf

    if c == 0:
        return 0

    if dp[a][b][c] != inf:
        return dp[a][b][c]

    if a < n-1:
        dp[a][b][c] = find_cost(a+1, b, c-1) + vertical_costs[a][b]
    if b < m-1:
        dp[a][b][c] = min(dp[a][b][c], find_cost(a, b+1, c-1) + horizontal_costs[a][b])
    if b > 0:
        dp[a][b][c] = min(dp[a][b][c], find_cost(a, b-1, c-1) + horizontal_costs[a][b-1])
    if a > 0:
        dp[a][b][c] = min(dp[a][b][c], find_cost(a-1, b, c-1) + vertical_costs[a-1][b])

    return dp[a][b][c]


ans = [[inf] * m for _ in range(n)]
if k % 2 == 1:
    for i in range(n):
        for j in range(m):
            ans[i][j] = -1
else:
    for i in range(n):
        for j in range(m):
            ans[i][j] = min(ans[i][j], 2 * find_cost(i, j, k//2))

for row in ans:
    print(*row)