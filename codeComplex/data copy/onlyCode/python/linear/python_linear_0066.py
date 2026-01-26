n, s = map(int, input().split())
ans = s
f = []
t = []
for i in range(n):
    f, t = map(int, input().split())
    if(t>(s-f)):
        ans +=  t - (s-f)
        s += t - (s-f)

print(ans)