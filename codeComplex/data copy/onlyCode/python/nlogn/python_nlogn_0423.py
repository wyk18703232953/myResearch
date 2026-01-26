import sys, heapq

def binary(num):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid
        else:
            return True
    return False

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
cnt = dict().fromkeys(set(arr), 0)
ans = 0
for i in arr:
    cnt[i] += 1
for i in range(n):
    now = arr[i]
    can = False
    for j in range(31):
        target = pow(2, j) - now
        if binary(target):
            if target == now:
                if cnt[now] >= 2:
                    can = True
                    break
            else:
                can = True
                break
    if not can:
        ans += 1
print(ans)