def main(n):
    # Deterministic data generation:
    # a: length of string
    # s: string consisting of 'H' and 'T' with a fixed pattern based on n
    a = n
    # Generate a deterministic pattern: alternate 'H' and 'T', then repeat pattern
    base = ['H' if i % 3 != 0 else 'T' for i in range(max(1, n))]
    s = ''.join(base[:n])

    d = s.count('H')
    p = []
    for i in range(len(s)):
        if i + d > len(s):
            nn = d + i - len(s)
            m = d - nn
            h = s[:m] + s[-nn:]
            k = h.count("T")
            p.append(k)

        else:
            h = s[i:d + i]
            k = h.count("T")
            p.append(k)
    mi = a
    for i in range(len(p)):
        if p[i] < mi:
            mi = p[i]
    if s.count("H") == 1 or s.count("T") == 0:
        # print(0)
        pass

    else:
        # print(mi)
        pass
if __name__ == "__main__":
    main(10)