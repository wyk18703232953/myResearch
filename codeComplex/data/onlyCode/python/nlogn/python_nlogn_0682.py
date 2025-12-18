N, M = map(int, input().split())
b = list(map(int, input().split()))
g = list(map(int, input().split()))

if max(b) > min(g):
    ans = -1
elif max(b) == min(g):
    ans = M*sum(b)
    maxi = max(b)
    for i in range(M):
        if maxi == g[i]:
            continue
        else:
            ans += g[i] - maxi
else:
    ans = M * sum(b)
    b.sort(reverse = True)
    for i in range(M):
        if i == 0:
            ans += g[i] - b[1]
        else:
            ans += g[i] - b[0]
print(ans)
