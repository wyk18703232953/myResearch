import sys


def input():
    return sys.stdin.readline().rstrip()


def slv():
    n, m, k = map(int, input().split())
    if k % 2 != 0:
        for i in range(n):
            print(*[-1]*m)
        return
    #always possible

    k //= 2

    DP = [[[0]*m for i in range(n)] for _ in range(k + 1)]
    G = [[[] for i in range(m)] for j in range(n)]
    for i in range(n):
        C = list(map(int,input().split()))
        for j in range(m - 1):
            cost = C[j]
            G[i][j].append((cost,i,j + 1))
            G[i][j + 1] .append((cost,i,j))

    for i in range(n - 1):
        C = list(map(int,input().split()))
        for j in range(m):
            cost = C[j]
            G[i][j].append((cost,i + 1,j))
            G[i+1][j].append((cost,i,j))


    for p in range(1,k + 1):
        for u in range(n):
            for v in range(m):
                DP[p][u][v] = min(DP[p - 1][x][y] + cost for (cost,x,y) in G[u][v])
    for i in range(n):
        ans = [DP[k][i][j]*2 for j in range(m)]
        print(*ans)
    return
def main():
    t = 1
    for i in range(t):
        slv()
    return


if __name__ == "__main__":
    main()
