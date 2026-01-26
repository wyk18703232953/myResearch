n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
d = []
for q in range(n):
    d.append(a[q]+s[q])
d = [n-q for q in d]
for q in range(n):
    f = 0
    for q1 in range(q):
        if d[q1] > d[q]:
            f += 1
    g = 0
    for q1 in range(q+1, n):
        if d[q1] > d[q]:
            g += 1
    if f != a[q] or g != s[q]:
        print('NO')
        break
else:
    print('YES')
    print(*d)
