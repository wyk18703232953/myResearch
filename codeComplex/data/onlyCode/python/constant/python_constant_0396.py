b = [list(input()) for _ in range(2)]

n = len(b[0])
ans = 0
a = []
for i in range(n):
    ai = 0
    if b[0][i] == '0':
        ai += 1
    if b[1][i] == '0':
        ai += 1
    a.append(ai)
prv = 0
for i in range(n):
    if a[i] == 0:
        prv = 0
    elif a[i] == 1:
        if prv == 2:
            ans += 1
            prv = 0
        else:
            prv = 1
    elif a[i] == 2:
        if prv == 2:
            ans += 1
            prv = 1
        elif prv == 1:
            ans += 1
            prv = 0
        else:
            prv = 2
print(ans)