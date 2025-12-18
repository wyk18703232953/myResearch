n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
for t in range(n):
    a[t].append(t+1)
a.sort()
for i in range(n-1):
    if a[i][1] >= a[i+1][1]:
        print(a[i+1][2],a[i][2])
        exit()
    if a[i][0] == a[i+1][0] and a[i][1] <= a[i+1][1]:
        print(a[i][2],a[i+1][2])
        exit()
print(-1,-1)