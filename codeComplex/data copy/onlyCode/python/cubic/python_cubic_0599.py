n, m, k = map(int, input().split())
DATA = [input() for i in range(n)]

#dp[n_day][used_cost]
#ans = min(dp[n_day][used_cost] for used_cost in range(k + 1))
#dp[n_day][used_cost] := min(dp[n_day - 1][prev_cost] + cost(pay used_cost - prev_cost in n_day) for prev_cost in range(used_cost + 1))
INF = 1 << 60
dp = [[INF]*(k + 10) for i in range(n + 10)]
dp[0][0] = 0

COST = [[INF]*(k + 10) for i in range(n + 10)]
for i, string in enumerate(DATA):
    #COST[i + 1]
    stack = []
    for j in range(m):
        if string[j] == "1":
            stack.append(j)
    L = len(stack)
    for j in range(k + 10):
        if j >= L:
            COST[i + 1][j] = 0
            continue
        else:
            for pos in range(j + 1):
                l = pos
                r = pos + L - 1 - j
                COST[i+1][j] = min(COST[i+1][j], stack[r] - stack[l] + 1)
for day in range(1, n + 1):
    for used_cost in range(k + 1):
        dp[day][used_cost] = min(dp[day - 1][prev_cost] + COST[day]
                                 [used_cost - prev_cost] for prev_cost in range(used_cost + 1))

ans = min(dp[n][used_cost] for used_cost in range(k + 1))
print(ans)
