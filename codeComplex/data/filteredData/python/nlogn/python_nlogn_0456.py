from collections import Counter


def main(n):
    # n: length of array l
    if n < 1:
        return

    # Deterministic construction of l and m
    # Ensure m is in l and is a "middle" value
    m = n // 2
    l = [(i * 2) % (n + 3) for i in range(n)]
    # Force at least one occurrence of m
    l[n // 2] = m

    # Original logic starts here
    p = l.index(m)
    le, ri = Counter(), Counter()
    c = 0
    le[0] = ri[0] = 1
    for i in range(p + 1, n):
        if l[i] < m:
            c += 1

        else:
            c -= 1
        ri[c] += 1
    c = 0
    for i in range(p - 1, -1, -1):
        if l[i] < m:
            c -= 1

        else:
            c += 1
        le[c] += 1
    res = 0
    for c, x in le.items():
        res += x * (ri[c] + ri[c - 1])
    # print(res)
    pass
if __name__ == "__main__":
    main(10)