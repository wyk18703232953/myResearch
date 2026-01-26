n = int(input())
dicta = {}
dictb = {}
for i in range(n):
    a, x = map(int, input().split())
    dicta[a] = x
m = int(input())
for i in range(m):
    b, y = map(int, input().split())
    dictb[b] = y
ans = 0
for i in dicta.keys():
    if i in dictb.keys():
        ans += max(dicta[i], dictb[i])
        del dictb[i]
    else :
        ans += dicta[i]
for i in dictb.values():
    ans += i
print(ans)
