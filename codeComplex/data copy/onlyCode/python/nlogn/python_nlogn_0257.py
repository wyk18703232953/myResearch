n, q = map(int, input().split())
A = list(map(int, input().split()))
K = list(map(int, input().split()))
from itertools import accumulate
C = [0]+A
C = list(accumulate(C))
total = 0
ans = [0]*q
import bisect
for i, k in enumerate(K):
    total += k
    j = bisect.bisect_right(C, total)
    if j != n+1:
        ans[i] = n-(j-1)
    else:
        ans[i] = n
        total = 0
print(*ans, sep='\n')
