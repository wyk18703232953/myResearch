n,x = list(map(int, input().split()))
arr = list(map(int, input().split()))
f = [0]*100100
s = [0]*100100
can = [False]*100100
for i in range(n):
    f[arr[i]]+=1
    s[arr[i]&x]+=1
    if (arr[i]&x != arr[i]):
        can[arr[i]&x] = True
ans = 3
for i in range(len(f)):
    if f[i] >= 2:
        ans = 0
        break
    if f[i] == 1 and s[i] >= 1:
        if can[i]:
            ans = min(ans,1)
    if s[i] >= 2:
        ans = min(ans,2)
if ans == 3:
    print(-1)
else:
    print(ans)
