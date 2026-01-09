from math import gcd
from collections import defaultdict as dd

def generate_expression(a, b, c):
    return f"({a}+{b})/{c}"

def main(n):
    m = max(1, n)
    d = dd(int)
    l = []
    ans = []

    for i in range(m):
        # 确定性生成 (a, b, c)
        a0 = i + 1
        b0 = (i * 2) % (m + 3) + 1
        c0 = (i * 3) % (m + 5) + 1

        s = generate_expression(a0, b0, c0)

        a = 0
        b = 0
        c = 0
        n_s = len(s)
        ind = 0

        for j in range(1, n_s):
            if s[j] == '+':
                ind = j + 1
                break
            a = a * 10 + int(s[j])

        for j in range(ind, n_s):
            if s[j] == ')':
                ind1 = j + 2
                break
            b = b * 10 + int(s[j])

        for j in range(ind1, n_s):
            c = c * 10 + int(s[j])

        a = a + b
        g = gcd(a, c)
        a = a // g
        c = c // g
        d[(a, c)] += 1
        l.append((a, c))

    for frac in l:
        ans.append(d[frac])

    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)