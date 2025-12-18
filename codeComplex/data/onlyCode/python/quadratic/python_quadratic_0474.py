n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
ans = [1 for i in range(n)]

s = [l[i] + r[i] for i in range(n)]
order = [i for i in range(n)]

for i in range(n-1):
    m = i
    for j in range(i+1,n):
        if s[m] < s[j]:
            m = j
    t = s[i]
    s[i] = s[m]
    s[m] = t
    t = order[i]
    order[i] = order[m]
    order[m] = t
cur = 1
for i in range(1,n):
    if s[i-1] > s[i]:
        cur += 1
    ans[order[i]] = cur
for i in range(n):
    k = 0
    for j in range(i):
        if ans[j] > ans[i]:
            k += 1
    if l[i] != k:
        print('NO')
        exit()
    k = 0
    for j in range(i+1,n):
        if ans[j] > ans[i]:
            k += 1
    if r[i] != k:
        print('NO')
        exit()

print('YES')
for i in ans:
    print(i, end=' ')