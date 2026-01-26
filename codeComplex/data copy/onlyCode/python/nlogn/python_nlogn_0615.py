import sys
import heapq
input = sys.stdin.readline

n,x,y = map(int,input().split())
MOD_NUM = 10**9+7

events = dict()
for i in range(n):
    l,r = map(int,input().split())
    if l not in events:
        events[l] = []
    events[l].append(r)

tv = []
pq = []
cost = 0

for t in sorted(events):
    while tv and tv[0] < t:
        heapq.heappush(pq, -(x + heapq.heappop(tv)*y))

    for ri in sorted(events[t],reverse=True):
        if pq and -pq[0] > t*y:
            val = -heapq.heappop(pq)
            rj = (val-x)//y

            cost += (ri-rj)*y
            heapq.heappush(tv, ri)
        else:
            cost += x + (ri-t)*y
            heapq.heappush(tv, ri)
    cost %= MOD_NUM

print(cost)
