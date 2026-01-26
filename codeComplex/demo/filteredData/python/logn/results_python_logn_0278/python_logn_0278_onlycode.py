def f(k):
    res = 1
    a = 2
    while k:
        if k % 2 == 1:
            res *= a
            k -= 1
        else:
            a *= a
            k //= 2
        res = res % (1000000007)
        a = a % (1000000007)
    return res


n, k = map(int, input().split())
if n == 0:
    print(0)
elif k == 0:
    print((n * 2) % 1000000007)
else:
    first = (2 * n - 1) % 1000000007
    first *= f(k)
    first = (first + 1) % 1000000007
    print(first)


