import sys, copy
 
 
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = [0] * (max(arr) + 1)
for i in arr:
    res[i] += 1
ans = 0
for d in range(1, m + 1):
    temp = copy.deepcopy(res)
    cnt = 0
    for i in range(len(temp)):
        while temp[i] >= d:
            temp[i] -= d
            cnt += 1
    if cnt >= n:
        ans = max(ans, d)
print(ans)