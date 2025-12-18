n, s = map(int, input().split())
ans = s
for i in range(n):
    f, t = map(int, input().split())
    ans = max(ans, t+f)
print(ans)