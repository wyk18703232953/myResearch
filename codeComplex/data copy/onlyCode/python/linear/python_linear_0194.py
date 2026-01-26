n, a, b, c, T = map(int, input().split())
ts = list(map(int, input().split()))
ts.sort()
ans = 0
for t in ts:
    temp = -10**18
    for u in range(t, T+1):
        temp = max(temp, c*(u-t)+a-b*(u-t))
        #print(temp)
    ans += temp
print(ans)
