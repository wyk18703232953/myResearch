import sys, heapq

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
q = []
for i in range(n):
    heapq.heappush(q, (-arr[i], i))
res = []
temp_k = k
while temp_k:
    val, idx = heapq.heappop(q)
    res.append((-val, idx))
    temp_k -= 1
res.sort(key=lambda x : x[1])
ans = 0
for i in res:
    ans += i[0]
path = []
cnt = 0
for i in range(n):
    if (arr[i], i) in res:
        path.append(cnt + 1)
        cnt = 0
    else:
        cnt += 1
path[-1] += n - sum(path)
print(ans)
print(' '.join(map(str, path)))