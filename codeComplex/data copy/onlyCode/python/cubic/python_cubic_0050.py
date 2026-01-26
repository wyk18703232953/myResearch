t = input()

n = len(t)

maxi = 0

for i in range(n):
    s = t[i]
    if t.count(s) > 1:
        maxi = max(maxi, 1)
    nr = 1
    for j in range(i + 1, n):
        s += t[j]
        nr += 1
        g = 0
        for h in range(n - nr + 1):
            if s == t[h:h + nr]:
                g += 1
        if g > 1:
            maxi = max(nr,maxi)

print(maxi)