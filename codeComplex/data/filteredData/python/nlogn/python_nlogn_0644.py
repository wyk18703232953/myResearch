from bisect import bisect_right as br
from bisect import bisect_left as bl

MAX = 10**9

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)

def main(n):
    if n < 0:
        n = 0
    m = 2 * n
    v = [i * 2 + 1 for i in range(n)]
    h = []
    for i in range(m):
        if i % 2 == 0:
            x1 = 1
            x2 = i * 3 + 1
            y = (i // 2) + 1

        else:
            x1 = 0
            x2 = i * 3 + 2
            y = (i // 2) + 2
        if x1 == 1:
            h.append(x2)
    lh = len(h)
    h.sort()
    v.sort()
    if not lh:
        # print(0)
        pass
    elif n == 0:
        # print(lh - bl(h, MAX))
        pass

    else:
        mn = n + lh - bl(h, MAX)
        for i in range(n):
            mn = min(mn, lh - bl(h, v[i]) + i)
        # print(mn)
        pass
if __name__ == "__main__":
    main(10)