def main(n):
    # Generate deterministic input array a of length n
    # Use simple arithmetic pattern to avoid zeros and keep variety
    if n <= 0:
        # print("")
        pass
        return
    a = [(i % 7) + 1 for i in range(1, n + 1)]

    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                elif any(a[j] > x and s[j] == 'B' for j in r):
                    s[i] = 'A'
                    m -= 1
    # print(''.join(s))
    pass
if __name__ == "__main__":
    main(10)