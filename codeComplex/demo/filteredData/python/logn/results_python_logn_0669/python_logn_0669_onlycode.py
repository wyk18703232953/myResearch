import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print('NO')
        continue
    n //= 2
    l, r = 0, n + 2
    while r - l > 1:
        m = (l + r) // 2
        if m * m <= n:
            l = m
        else:
            r = m
    if l * l == n:
        print('YES')
        continue
    l, r = 0, n + 2
    while r - l > 1:
        m = (l + r) // 2
        if m * m * 2 <= n:
            l = m
        else:
            r = m
    if l * l * 2 == n:
        print('YES')
        continue
    print('NO')