n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
ok = False
for i in range(len(a)):
    if (a[i] > min(a) ):
        ans = a[i]
        ok = True
        break
if (ok):
    print(ans)
else:
    print("NO")