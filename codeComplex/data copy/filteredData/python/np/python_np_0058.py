import math

def main(n):
    # Deterministically generate s and p based on n
    # s and p have length n
    s = []
    p = []
    for i in range(n):
        # For s: alternate '+' and '-' deterministically
        if i % 2 == 0:
            s.append('+')
        else:
            s.append('-')
        # For p: pattern with '+', '-', and '?' to ensure all cases
        t = i % 3
        if t == 0:
            p.append('+')
        elif t == 1:
            p.append('-')
        else:
            p.append('?')
    s = ''.join(s)
    p = ''.join(p)

    c = 1
    ss = 0
    ps = 0
    k = 0
    for i in range(len(s)):
        if p[i] == '?':
            c *= 2
            k += 1
        if s[i] == '+':
            ss += 1
        else:
            ss -= 1
        if p[i] == '+':
            ps += 1
        elif p[i] == '-':
            ps -= 1
    y = math.fabs(ss - ps)
    x = k - y
    a = y + x / 2
    b = k - a
    if k < y:
        ans = 0.000000000
    else:
        ans = math.factorial(int(a + b)) / (math.factorial(int(a)) * math.factorial(int(b)))
        ans /= c
    print("%.12f" % ans)


if __name__ == "__main__":
    main(10)