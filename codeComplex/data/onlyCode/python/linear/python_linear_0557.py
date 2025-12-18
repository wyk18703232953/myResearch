n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
for i in range(n):
    ai = a[i]
    nai = ((1<<k) - 1)^ai
    if nai < ai:
        a[i] = nai

from collections import Counter
C = Counter()
C[0] += 1
S = 0
cnt = 0
for j, ai in enumerate(a):
    nai = ((1<<k) - 1)^ai
    v1, v2 = C[S^ai], C[S^nai]
    if v1 <= v2:
        cnt += j + 1 - v1
        S ^= ai
        C[S] += 1
    else:
        cnt += j + 1 - v2
        S ^= nai
        C[S] += 1
print(cnt)
    
