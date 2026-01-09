def main(n):
    # Generate deterministic input of size n
    # a is a list of integers with values from 1 to n (avoid zero to prevent modulo by zero)
    a = [(i % n) + 1 for i in range(n)]

    b = [0] * n  # unused in original code but kept for structure
    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if s[i] == 0:  # ensure second condition checks only if still unset
                    if any(a[j] > x and s[j] == 'B' for j in r):
                        s[i] = 'A'
                        m -= 1
                if m == 0:
                    break
    # print(''.join(s))
    pass
if __name__ == "__main__":
    main(10)