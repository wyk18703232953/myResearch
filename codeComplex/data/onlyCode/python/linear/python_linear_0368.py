n, m = map(int, input().split())
k = list(map(int, input().split()))
p = list(map(int, input().split()))
a = 0
b = 0
ans = 0
while a != n and b != m:
    if p[b] >= k[a]:
        ans += 1
        a += 1
        b += 1
    else:
        a += 1
print(ans)
