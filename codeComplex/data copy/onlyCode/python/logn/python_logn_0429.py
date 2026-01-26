f = [0 for _ in range(40)]

for i in range(1, 32):
    f[i] = 1 + 4 * f[i - 1]
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n >= 32:
        print("YES %d" % (n - 1))
        continue

    if f[n] < k:
        print("NO")
        continue

    k -= 1
    extra = 1
    way = 3
    size = n - 1
    done = False
    total = f[size]
    ans = True
    while k > total and size > 0:
        if k < way:
            ans = False
            break
        k -= way
        size -= 1
        extra = way * 2 - 1
        way = way * 2 + 1
        total += extra * f[size]

    if ans:
        print("YES %d" % size)
    else:
        print("NO")
