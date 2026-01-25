from math import gcd
from collections import defaultdict as dd

def parse_expression(s):
    a = 0
    b = 0
    c = 0
    n = len(s)
    ind = 0
    # parse a
    for i in range(1, n):
        if s[i] == '+':
            ind = i + 1
            break
        a = a * 10 + int(s[i])
    # parse b
    for i in range(ind, n):
        if s[i] == ')':
            ind1 = i + 2
            break
        b = b * 10 + int(s[i])
    # parse c
    for i in range(ind1, n):
        c = c * 10 + int(s[i])
    a = a + b
    g = gcd(a, c)
    a = a // g
    c = c // g
    return a, c

def main(n):
    m = n
    d = dd(int)
    l = []
    ans = []

    # deterministic expression generation:
    # s = f"({a}+{b})/{c}"
    # a, b, c depend only on i and m, so are deterministic
    for i in range(m):
        a = i + 1
        b = (m - i) // 2 + 1
        c = (i * 2 + 3) if (i * 2 + 3) != 0 else 1
        s = "(" + str(a) + "+" + str(b) + ")/" + str(c)
        a_norm, c_norm = parse_expression(s)
        d[(a_norm, c_norm)] += 1
        l.append((a_norm, c_norm))

    for frac in l:
        ans.append(d[frac])

    print(*ans)

if __name__ == "__main__":
    main(10)