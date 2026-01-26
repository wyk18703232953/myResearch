import sys, heapq

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = dict().fromkeys(set(arr), 0)
for i in arr:
    res[i] += 1
can = False
for i in res:
    if res[i] >= 2:
        can = True
        break
if can:
    print(0)
else:
    res = dict().fromkeys([i for i in range(max(arr) + 1)])
    for i in res:
        res[i] = []
    for i in range(n):
        temp = set()
        now = arr[i]
        cnt = 0
        while True:
            added = False
            before = len(temp)
            temp.add(now)
            after = len(temp)
            if before == after:
                break
            heapq.heappush(res[now], cnt)
            now = now & x
            cnt += 1
    ans = 9876543210
    for i in res:
        if len(res[i]) >= 2:
            ans = min(ans, heapq.heappop(res[i]) + heapq.heappop(res[i]))
    print(ans if ans != 9876543210 else -1)