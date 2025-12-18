n = int(input())
a = list(input())
smm = 0
for i in range(n):
    a[i] = int(a[i])
    smm += a[i]
ans = "NO"
sm = smm
for div in range(2, n + 1):
    sm = smm
    if not sm % div:
        sm //= div
        f = 0
        s = 0
        for i in range(n):
            s += a[i]
            if s == sm:
                s = 0
                f += 1
        if f == div:
            ans = "YES"
            break
print(ans)
