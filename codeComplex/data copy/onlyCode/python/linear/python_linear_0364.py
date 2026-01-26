n ,m  = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(len(a)):
    if (len(b) == 0):
        break
    if (b[0] >= a[i]):
        ans += 1
        del b[0]
print(ans)
