import math

def valid(n, k, c1, c2):
    if c1 > n:
        return c2
    elif c2 > n:
        return c1
    ans_one = ((n - c1) * (n - c1 + 1) // 2) - c1
    if ans_one == k:
        return c1
    return c2


def f(n, k):
    b2 = (2 * n + 3)
    delta = int(math.sqrt(8 * n + 8 * k + 9))
    return valid(n, k, (b2 + delta) // 2, (b2 - delta) // 2)


n, k = map(int, input().strip().split(' '))
print(f(n, k))
