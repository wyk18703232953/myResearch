n,m = map(int,input().split())
for _ in range(m):
    x,y = map(int,input().split())

cnt = 0
ans = []
for i in range(n):
    if cnt%2 == 0:
        ans.append("0")

    else:
        ans.append("1")

    cnt += 1

print("".join(ans))