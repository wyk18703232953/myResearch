import io, os, sys

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def read():
    n, m, k = map(int, input().split() )    

    h = [list(map(int, input().split() ) )+ [float("+inf")] for _ in range(n)]


    v = [list(map(int, input().split() ) ) for _ in range(n-1)]
    v.append( [float("+inf")] * m )

    solve(n, m, k, h, v)

def solve(n, m, k, h, v):
    if k % 2:
        ans = "-1 " * m
        for _ in range(n):
            print(ans)
        return
    
    #inf = float("+inf")

    dp = [ [0] * (m+1) for _ in range(n+1)]

    nxt = [ [0] * (m+1) for  _ in range(n+1)]

    for _ in range(2, k + 1, 2):

        for i in range(n):
            for j in range(m):
                l = 2 * h[i][j-1] + dp[i][j-1]
                r = 2 * h[i][j]  + dp[i][j+1]
                u = 2 * v[i-1][j] + dp[i-1][j]
                d = 2 * v[i][j]  + dp[i+1][j]

                hor = min(l, r)
                ver = min(u, d)

                nxt[i][j] = min(hor, ver)

        dp, nxt = nxt, dp

    for l in dp[:-1]:
        print(" ".join(map(str, l[:-1])))




if __name__ == "__main__":
    read()