from math import gcd
from collections import defaultdict as dd

def main(n):
    # n: number of expressions (input lines)
    m = n

    d = dd(int)
    l = []

    # Deterministic generation of m strings of the form "(a+b)/c"
    # where a, b, c are positive integers depending on line index i
    for idx in range(m):
        # Generate a, b, c deterministically from idx
        a_val = idx + 1
        b_val = (idx * 2) + 3
        c_val = (idx % 5) + 2

        s = "(" + str(a_val) + "+" + str(b_val) + ")/" + str(c_val)

        a = 0
        b = 0
        c = 0
        n_len = len(s)
        ind = 0

        for i in range(1, n_len):
            if s[i] == '+':
                ind = i + 1
                break
            a = a * 10 + int(s[i])

        for i in range(ind, n_len):
            if s[i] == ')':
                ind1 = i + 2
                break
            b = b * 10 + int(s[i])

        for i in range(ind1, n_len):
            c = c * 10 + int(s[i])

        a = a + b
        g = gcd(a, c)
        a = a // g
        c = c // g
        d[(a, c)] += 1
        l.append((a, c))

    for key in l:
        # print(d[key], end=" ")
        pass
if __name__ == "__main__":
    main(10)