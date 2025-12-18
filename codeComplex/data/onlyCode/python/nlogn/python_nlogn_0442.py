from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
x = [0] * (n + 1)
for i in range(n):
    if p[i] < m:
        x[i + 1] = -1
    elif p[i] > m:
        x[i + 1] = 1
    else:
        l = i
for i in range(1, n + 1):
    x[i] += x[i - 1]
cnt = [defaultdict(lambda : 0) for _ in range(2)]
for i in range(l + 1):
    cnt[i % 2][x[i]] += 1
ans = 0
for i in range(l + 1, n + 1):
    xi = x[i]
    ans += cnt[i % 2][xi - 1]
    ans += cnt[i % 2 ^ 1][xi]
print(ans)