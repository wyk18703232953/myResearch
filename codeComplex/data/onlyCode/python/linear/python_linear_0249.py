from sys import stdin

n, k = map(int, stdin.readline().split())
out = [['.'] * n for _ in range(4)]
if k & 1:
    out[1][n >> 1] = '#'
    k -= 1

for i in range(1, 3):
    l, r = 1, n - 2
    for j in range(1, n - 2):
        if k:
            k -= 1
            if j & 1:
                out[i][l] = '#'
                l += 1
            else:
                out[i][r] = '#'
                r -= 1

for i in range(1, 3):
    if k:
        k -= 1
        out[i][n >> 1] = '#'
print('YES\n%s' % ('\n'.join([''.join(x) for x in out])))
