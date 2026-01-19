import io
import os
from collections import defaultdict as dd

def main(n):
    # Map n to matrix size
    # Ensure at least 1x1
    n = max(1, n)
    m = max(1, n // 2)

    # Deterministic generation of input matrix of size n x m
    # a[i][j] = (i+1)*10 + (j+1) for determinism and monotonic growth
    matrix = [[(i + 1) * 10 + (j + 1) for j in range(m)] for i in range(n)]

    l = []
    an = -1
    a = b = 0

    for idx in range(n):
        k = matrix[idx]
        # original code appends row values plus row index at the end
        l.append(k + [idx + 1])
        if an < min(k):
            a = b = idx + 1
            an = min(k)

    le = an
    r = 10 ** 9 + 1
    while le < r:
        md = (le + r) // 2
        f = 0
        a1 = a2 = -1
        s = [0] * n
        for i in range(n):
            for j in range(m):
                if l[i][j] >= md:
                    s[i] |= 1 << j

        po = 1 << m
        d = [0] * po
        for i in range(n):
            d[s[i]] = i + 1
        for i in range(1, po):
            if d[i]:
                pp = i
                while pp:
                    d[pp] = d[i]
                    pp = (pp - 1) & i
        if d[po - 1]:
            f = 1
            a1 = a2 = d[po - 1]
        for i in range(1, po):
            if d[i] and d[(po - 1) ^ i]:
                f = 1
                a1 = d[i]
                a2 = d[(po - 1) ^ i]
                break
        if f:
            le = md + 1
            if md > an:
                a, b = a1, a2
                an = md
        else:
            r = md
    print(a, b)


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)