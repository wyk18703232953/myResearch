import sys
from math import inf, ceil

def prod(a, mod=10 ** 9 + 7):
    ans = 1
    for each in a:
        ans = (ans * each) % mod
    return ans

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(a, b):
    return a * b // gcd(a, b)

def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y

def run_once(n, m, a):
    alpha, omega = 0, 10**9

    def solve(mid):
        index = [-1] * (1 << m)
        for i in range(n):
            val = 0
            for j in range(m):
                if a[i][j] >= mid:
                    val += (1 << j)
            index[val] = i + 1
        pos = False
        full = (1 << m) - 1
        for mask in range(1 << m):
            for mask2 in range(1 << m):
                if mask | mask2 != full:
                    continue
                if min(index[mask], index[mask2]) != -1:
                    pos = (index[mask], index[mask2])
                    break
            if pos:
                break
        return pos

    while alpha < omega:
        mid = (alpha + omega + 1) // 2
        if solve(mid):
            alpha = mid
        else:
            omega = mid - 1
    return solve(alpha)

def main(n):
    if n <= 0:
        return
    m = 0
    while (1 << m) < n and m < 30:
        m += 1
    if m == 0:
        m = 1
    a = [[(i + 1) * (j + 2) % (10**9 + 7) for j in range(m)] for i in range(n)]
    i1, i2 = run_once(n, m, a)
    print(i1, i2)

if __name__ == "__main__":
    main(8)