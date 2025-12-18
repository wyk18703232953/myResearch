n,m = map(int, input().split())
b = [int(s) for s in input().split()]
g = [int(s) for s in input().split()]
ans = 0
maxb2, maxb = sorted(b)[-2:]
ming = min(g)
if maxb > ming:
    ans = -1
else:
    ans += sum(b)*m
    ans += (sum(g)-ming)-(maxb*(m-1))
    if ming > maxb:
        ans += ming-maxb2
print(ans)