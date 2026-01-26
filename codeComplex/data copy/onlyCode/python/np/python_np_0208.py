n, l, r, x = map(int, input().split())
tasks = list(map(int, input().split()))
mask = 3
ans = 0

while (mask < (1 << n)):
    sum_dif = 0
    min_diff = float("inf")
    max_diff = -float("inf")

    if (mask & (mask-1)):
        for i in range(n):
            if (mask & (1 << i)):
                sum_dif += tasks[i]
                min_diff = min(min_diff, tasks[i])
                max_diff = max(max_diff, tasks[i])
        if (x <= (max_diff - min_diff)) and (l <= sum_dif <= r):
            ans += 1

    mask += 1

print(ans)