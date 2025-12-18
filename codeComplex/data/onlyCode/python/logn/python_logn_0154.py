def inp():
    return map(int, input().split())


def sum_range(n):
    return (n * (n + 1)) // 2


def bs(st, en):
    while (st < en):
        mid = st + (en - st) // 2
        s1 = s - sum_range(mid - 1)

        if s1 == n:
            return (k - mid) + 1
        elif s1 > n:
            st = mid + 1
        else:
            en = mid
    return (k - st) + 2


n, k = inp()
n -= 1
k -= 1
s = sum_range(k)

if n+1 == 1:
    print(0)
elif n <= k:
    exit(print(1))
elif n > s:
    print(-1)
else:
    print(bs(1, k))
