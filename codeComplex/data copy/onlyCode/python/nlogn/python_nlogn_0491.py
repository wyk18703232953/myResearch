n,m = map(int,input().split())
ans = 0
temp = [0 for i in range(n)]
for i in range(n):
    l,r = map(int,input().split())
    ans += l
    temp[i] = l-r
temp.sort(reverse=True)

if ans<=m:
    print(0)
else:
    for i in range(n):
        ans -= temp[i]
        if ans<=m:
            print(i+1)
            break
    else:
        print(-1)
