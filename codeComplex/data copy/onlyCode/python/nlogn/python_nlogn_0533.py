from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().rstrip().split()))
cnt = [defaultdict(lambda : 0) for _ in range(11)]
for i in a:
    cnt[len(str(i))][i % k] += 1
ans = 0
d = 10
for i in range(1, 11):
    cnti = cnt[i]
    for j in a:
        ans += cnti[(k - d * j) % k]
    d *= 10
for i in a:
    if not int(str(i) * 2) % k:
        ans -= 1
print(ans)