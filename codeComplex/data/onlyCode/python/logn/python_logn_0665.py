import sys, collections

n, k = map(int, sys.stdin.readline().split())
left = 0
right = n + 1
while left < right:
    mid = (left + right) // 2
    candy = n - mid
    total = (candy * (candy + 1)) // 2 - mid
    if total < k:
        right = mid
    elif total > k:
        left = mid + 1
    else:
        print(mid)
        break