def main():
    n, m, k = [int(v) for v in input().split()]
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, -1, 1]
    w = [[[0 for d in range(4)] for j in range(m)] for i in range(n)]
    for i in range(n):
        row = [int(v) for v in input().split()]
        for j in range(m-1):
            w[i][j+1][2] = row[j]
            w[i][j][3] = row[j]
    for i in range(n-1):
        row = [int(v) for v in input().split()]
        for j in range(m):
            w[i][j][1] = row[j]
            w[i+1][j][0] = row[j]
    if k % 2 == 1:
        for i in range(n):
            for j in range(m):
                print(-1, end=" ")
            print()
        return
    else:
        k //= 2
    dp = [[[int(40 * 1e6) for d in range(k+1)] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j][0] = 0
    for d in range(1, k+1):
        for i in range(n):
            for j in range(m):
                for di, (dx, dy) in enumerate(dxy):
                    ii = i + dx
                    jj = j + dy
                    if 0 <= ii < n and 0 <= jj < m:
                        dp[i][j][d] = min(dp[i][j][d], dp[ii][jj][d-1] + w[i][j][di])
    for i in range(n):
        for j in range(m):
            print(dp[i][j][k] * 2, end=" ")
        print()

main()

