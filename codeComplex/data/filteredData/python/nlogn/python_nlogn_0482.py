def main(n):
    # Generate deterministic k and array a based on n
    # Ensure k >= n so that k//n is meaningful and can be non-zero for some n
    k = 2 * n + 5
    a = [(i % (n // 2 + 1)) + 1 for i in range(n)]

    d = {}
    for chr in a:
        if chr not in d:
            d[chr] = 1
        else:
            d[chr] += 1
    p = list(d.values())
    z = k // n
    if z == 0:
        print(0)
    else:
        o = []
        if len(a) >= n:
            o.append(1)
        for i in range(2, z + 1):
            c = 0
            for j in range(len(p)):
                c += p[j] // i
            if c >= n:
                o.append(i)
        print(max(o))


if __name__ == "__main__":
    main(10)