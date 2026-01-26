a = int(input())
s = {}
ans = 0
for i in range(a - 1):
    v, c = map(int, input().split())
    if v in s:
        s[v].append(c)
    else:
        s[v] = [c]
    if c in s:
        s[c].append(v)
    else:
        s[c] = [v]
c = 0
for i in range(1, a + 1):
    if len(s[i]) > 2:
        c += 1
        ans = i
if c > 1:
    print("No")
elif c == 0:
    print("Yes")
    print(1)
    for i in s:
        if len(s[i]) == 1:
            print(i, end=" ")
else:
    print("Yes")
    print(len(s[ans]))
    k = []
    for i in s:
        if len(s[i]) == 1:
            k.append(i)
    for i in k:
        print(min(ans, i), max(ans, i))
