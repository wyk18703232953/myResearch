import sys, heapq

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
pf = [0] * (n + 1)
pf[0] = arr[0]
for i in range(1, n):
    pf[i] = pf[i - 1] + arr[i]
ans = 0
for i in range(n):
    for j in range(n):
        left = i
        right = j
        if right - left + 1 >= k:
            temp = pf[right] - pf[left - 1]
            ans = max(ans, temp / (right - left + 1))
print(ans)