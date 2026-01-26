from heapq import heappush, heappop
n,k = map(int, input().split())
powers = list(map(int, input().split()))
coins = list(map(int, input().split()))

A = []
ans = [0] * n
for i in range(n):
    A.append((powers[i], coins[i], i))
A.sort()
h = []
total = 0
for i in range(n):
    _,c,idx = A[i]
    ans[idx] = total + c
    if len(h) < k:
        heappush(h, c)
        total += c
    elif h and h[0] < c:
        total -= heappop(h)
        heappush(h, c)
        total += c

for x in ans:
    print(x, end=" ")
print()
