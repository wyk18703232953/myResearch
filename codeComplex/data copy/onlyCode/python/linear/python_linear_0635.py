t = int(input())

for iter in range(t):
    n, k = map(int, input().split())
    if n >= 50:
        if k == 0:
            print("YES " + str(n))
        else:
            print("YES " + str(n - 1))
    else:
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        c = [0] * (n + 1)
        a[0] = 0
        b[n] = 1
        c[n] = 0

        for i in range(1, n + 1):
            a[i] = 4 * a[i - 1] + 1
        for i in range(n - 1, -1, -1):
            b[i] = b[i + 1] * 2 + 1
        for i in range(n - 1, -1, -1):
            c[i] = c[i + 1] + b[i + 1]

        res = -1
        for d in range(n + 1):
            if c[d] <= k and k <= a[n] - a[d] * b[d]:
                res = d

        if res == -1:
            print("NO")
        else:
            print("YES " + str(res))
