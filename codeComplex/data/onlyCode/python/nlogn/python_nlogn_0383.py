n,k = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
Q = []
for i, p in enumerate(P):
    Q.append((p, i))
Q.sort()
q = []
import heapq
heapq.heapify([])
s = 0
ans = [0]*n
if k > 0:
    for p, i in Q:
        ans[i] = s+C[i]
        if len(q) == k:
            if q[0] <= C[i]:
                v = heapq.heappop(q)
                heapq.heappush(q, C[i])
                s -= v
                s += C[i]
        else:
            heapq.heappush(q, C[i])
            s += C[i]
    print(*ans)
else:
    for p, i in Q:
        ans[i] = C[i]
    print(*ans)
