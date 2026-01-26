def main():
    high = 10 ** 12
    n, m, k = map(int, input().split())
    hozs = []
    for i in range(n):
        hozs.append(list(map(int, input().split())))
    verts = []
    for i in range(n - 1):
        verts.append(list(map(int, input().split())))
    if k % 2:
        for i in range(n):
            print("-1 " * m)
        return
    k //= 2
    dp = []
    for i in range(n):
        dp.append([])
        for j in range(m):
            dp[-1].append([])
            for kay in range(k + 1):
                dp[-1][-1].append(0)
    for depth in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                if i == 0:
                    up = high
                else:
                    up = verts[i - 1][j] + dp[i - 1][j][depth - 1]
                if i == n - 1:
                    down = high
                else:
                    down = verts[i][j] + dp[i + 1][j][depth - 1]
                if j == 0:
                    left = high
                else:
                    left = hozs[i][j - 1] + dp[i][j - 1][depth - 1]
                if j == m - 1:
                    right = high
                else:
                    right = hozs[i][j] + dp[i][j + 1][depth - 1]
                min_cost = min(up, down, left, right)
                ''''
                if min_cost == up:
                    dp[i][j][depth] = dp[i - 1][j][depth - 1]
                elif min_cost == down:
                    dp[i][j][depth] = dp[i + 1][j][depth - 1]
                elif min_cost == left:
                    dp[i][j][depth] = dp[i][j - 1][depth - 1]
                else:
                    dp[i][j][depth] = dp[i][j + 1][depth - 1]
                '''
                dp[i][j][depth] += min_cost
    for i in range(n):
        print(*[2 * dp[i][j][k] for j in range(m)])
main()