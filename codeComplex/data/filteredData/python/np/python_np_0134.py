def main(n):
    # Generate deterministic input data based on n
    # n is the number of elements in lists l and c
    l = [i + 2 for i in range(n)]
    c = [(i % 5) + 1 for i in range(n)]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    a = {0: 0}
    for i in range(n):
        b = a.copy()
        for key, val in a.items():
            d = gcd(key, l[i])
            cost = val + c[i]
            if d not in b:
                b[d] = cost
            elif b[d] > cost:
                b[d] = cost
        a = b

    if 1 not in a:
        a[1] = -1
    print(a[1])


if __name__ == "__main__":
    main(10)