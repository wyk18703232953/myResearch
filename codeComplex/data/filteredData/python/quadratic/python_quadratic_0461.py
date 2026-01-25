def main(n):
    # ensure n is positive
    if n <= 0:
        return ""

    # deterministic generation of a with clear structure
    # mix increasing and modular pattern to avoid trivial uniform data
    a = [i % (n // 2 + 1) + 1 for i in range(1, n + 1)]

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
                if any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
    result = ''.join(s)
    return result


if __name__ == "__main__":
    # example: run for a specific n to observe behavior or for timing
    n = 10
    print(main(n))