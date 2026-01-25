def main(n):
    if n <= 0:
        print("")
        return

    # Deterministic construction of a length-n array a of positive integers
    # Avoid zeros to prevent division issues in the original logic
    a = [(i % 7) + 1 for i in range(n)]

    s = [0] * n
    m = n
    # Preserve original algorithm; note that zero values in s are used as "unassigned"
    while m:
        for i, x in enumerate(a):
            r = range(i % x, n, x)
            if s[i] == 0:
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
                if m == 0:
                    break
    print(''.join(s))


if __name__ == "__main__":
    # Example deterministic call; change the value to test other scales
    main(10)