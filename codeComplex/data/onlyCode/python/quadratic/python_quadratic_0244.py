def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n, a, b = mi()
c = max(a, b)
if a != 1 and b != 1:
    print('NO')
elif n == 2 and c == 1:
    print('NO')
elif n == 3 and c == 1:
    print('NO')
else:
    if a == 1:
        g = [[1] * n for i in range(n)]
        for i in range(n):
            g[i][i] = 0
        for i in range(c - 1, n - 1):
            g[i][i + 1] = g[i + 1][i] = 0
    else:
        g = [[0] * n for i in range(n)]
        for i in range(c - 1, n - 1):
            g[i][i + 1] = g[i + 1][i] = 1
    print('YES')
    for r in g:
        print(''.join(str(x) for x in r))