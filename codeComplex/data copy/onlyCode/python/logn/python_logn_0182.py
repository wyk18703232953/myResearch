from sys import stdin

n, m = map(int, stdin.readline().split())
be, en, ans = 1, n, n + 1
while be <= en:
    md = (be + en) >> 1
    if md - sum(int(x) for x in str(md)) >= m:
        en = md - 1
        ans = md
    else:
        be = md + 1

print(n - ans + 1)
