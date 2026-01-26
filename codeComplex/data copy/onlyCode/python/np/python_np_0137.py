from sys import stdin

n, m = map(int, stdin.readline().split())
ans, p, all = [], [1 << i for i in range(n - 2, -1, -1)] + [1], set(range(1, n + 1))
num, cur, i = 1, 0, 0

while i < len(p) and m > 0 and num <= n:
    cur += p[i]
    if cur >= m:
        m -= (cur - p[i])
        cur = 0
        ans.append(num)
        all.discard(num)
    num += 1
    i += 1

print(' '.join(map(str, ans + sorted(all)[::-1])))
