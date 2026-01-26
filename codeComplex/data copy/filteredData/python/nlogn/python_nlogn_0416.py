def modinv(n, p):
    return pow(n, p - 2, p)

def ncr(n, r, p, f):
    t = (f[n] * (modinv(f[r], p) % p) * (modinv(f[n - r], p) % p)) % p
    return t

mod = (10 ** 9) + 7

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def BS(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BS(arr, l, mid - 1, x)

        else:
            return BS(arr, mid + 1, r, x)

    else:
        return -1

from bisect import bisect_left as bl
from bisect import bisect_right as br
import itertools
import math
from Queue import Queue as Q

def main(n):
    # Deterministic generation of n intervals [l, r]
    # Example pattern: l = i, r = 2*i for i in 1..n
    p = []
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        l = i
        r = 2 * i
        p.append([l, "l"])
        p.append([r, "r"])

    p.sort(key=lambda x: x[0])
    o = 1
    c = 0
    w = []
    for i in range(1, len(p)):
        if p[i][0] == p[i - 1][0]:
            if p[i][1] == "l":
                o += 1

            else:
                c += 1

        else:
            w.append([p[i - 1][0], o, c])
            o, c = 0, 0
            if p[i][1] == "l":
                o = 1

            else:
                c = 1
    w.append([p[-1][0], o, c])
    s = 0
    i = 0
    r = -1
    while i < len(w):
        f[s] += w[i][0] - r - 1
        f[s + w[i][1]] += 1
        s += w[i][1] - w[i][2]
        r = w[i][0]
        i += 1

    output = []
    for i in range(1, n + 1):
        output.append(str(f[i]))
    # print(" ".join(output))
    pass
if __name__ == "__main__":
    main(10)