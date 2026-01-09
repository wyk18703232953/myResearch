def main(n):
    # Generate deterministic input data based on n
    # Original program expects:
    # n: integer
    # a: list of n integers
    # Here we choose a simple deterministic sequence
    # to ensure behavior is scalable and repeatable.
    if n <= 0:
        # print("")
        pass
        return

    # Deterministic array a of length n
    # Example: a[i] = i % 7 + 1 (all positive, avoid zero for modulo operations)
    a = [(i % 7) + 1 for i in range(n)]

    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
                if m == 0:
                    break
    # print(''.join(s))
    pass
if __name__ == "__main__":
    # Example call for experimental purposes
    main(10)