n = int(input())
a = {}
ans = 0
sum = 0
i = 0
for t in map(int, input().split()):
    sum += t
    a[t] = a.get(t, 0) + 1

    ans += (i - a.get(t, 0) - a.get(t - 1, 0) - a.get(t + 1, 0) + 1) * t - (sum - a.get(t, 0) * t - a.get(t - 1, 0) * (t - 1) - a.get(t + 1, 0) * (t + 1))
    i += 1
            
print(ans)
