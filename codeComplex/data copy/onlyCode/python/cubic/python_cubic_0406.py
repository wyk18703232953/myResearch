import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, m, k = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n-1):
        b.append(list(map(int, input().split())))
    if k % 2:
        ans = [-1] * m
        for i in range(n):
            print(*ans)
        return 
    k //= 2
    pre = [[0]*m for i in range(n)]
    cur = [[10**9]*m for i in range(n)]
    for _ in range(k):
        cur = [[10**9] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    cur[i][j] = min(cur[i][j], pre[i-1][j]+b[i-1][j])
                if i < n - 1:
                    cur[i][j] = min(cur[i][j], pre[i+1][j]+b[i][j])
                if j:
                    cur[i][j] = min(cur[i][j], pre[i][j-1]+a[i][j-1])
                if j < m - 1:
                    cur[i][j] = min(cur[i][j], pre[i][j+1]+a[i][j])
        pre = cur
    for i in range(n):
        cur[i] = [cur[i][j]*2 for j in range(m)]
        print(*cur[i])





solve()

