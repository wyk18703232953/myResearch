def main(n):
    # Ensure n is positive
    if n <= 0:
        # print("")
        pass
        return

    # Deterministic construction of a based on n
    # a[i] = (i % n) + 1 to avoid zeros in modulus
    a = [(i % n) + 1 for i in range(n)]

    b = [0] * n
    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if s[i] == 0:
                    if any(a[j] > x and s[j] == 'B' for j in r):
                        s[i] = 'A'
                        m -= 1
    # print(''.join(s))
    pass
if __name__ == "__main__":
    main(10)