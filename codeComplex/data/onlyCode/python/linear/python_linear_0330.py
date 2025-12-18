n, M = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

a.insert(0, 0)
n += 1

lit = [0] * (n + 1)
for i in range(1, n):
    if i % 2 == 0:
        lit[i] = lit[i - 1]
    else:
        lit[i] = lit[i - 1] + a[i] - a[i - 1]
if n % 2 == 0:
    lit[n] = lit[n - 1]
else:
    lit[n] = lit[n - 1] + M - a[n - 1]
# print(lit)

ans = lit[n]
for i in range(n):
    pre_lit = lit[i]
    post_lit = M - a[i] - (lit[n] - lit[i])    
    # print(i, pre_lit, post_lit)
    if i > 0 and a[i - 1] + 1 < a[i]:
        if i % 2 == 0:
            ans = max(ans, pre_lit + 1 + post_lit)
        else:
            ans = max(ans, pre_lit - 1 + post_lit)
    if (i + 1 < n and a[i] + 1 < a[i + 1]) or (i + 1 == n and a[n - 1] + 1 < M):
        if i % 2 == 0:
            ans = max(ans, pre_lit + post_lit + 1)
        else:
            ans = max(ans, pre_lit + post_lit - 1)    
print(ans)