import sys
input = sys.stdin.readline

'''

'''

from heapq import heapify, heappush, heappop

n, k = map(int, input().split())
plst = list(map(int, input().split()))
clst = list(map(int, input().split()))

if k == 0:
    print(*clst)
    sys.exit()

pc = sorted(((p, c, i) for i, (p, c) in enumerate(zip(plst, clst))), key=lambda t: (t[0], t[2]))
res = [0] * n
pq = []
pq_sum = 0
pq_size = 0

for p, c, i in pc:
    if i > 0 and plst[i] == plst[i-1]:
        res[i] = res[i-1]
    else:
        res[i] = pq_sum + c

    # Update pq
    if pq_size < k:
        heappush(pq, c)
        pq_sum += c
        pq_size += 1
    else:
        alt = heappop(pq)
        if alt < c:
            heappush(pq, c)
            pq_sum += c - alt
        else:
            heappush(pq, alt)

print(*res)
