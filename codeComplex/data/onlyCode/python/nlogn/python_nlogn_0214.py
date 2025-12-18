n, u = map(int, input().split())
e = list(map(int, input().split()))
ans = -1
k = 2
for i in range(n-2):
    while k<n-1 and e[k+1] - e[i] <= u:
        k+=1
    if i < k-1 and e[k] - e[i] <= u:
        ans = max(ans,(e[k]-e[i+1]) / (e[k]-e[i]))
print(ans)