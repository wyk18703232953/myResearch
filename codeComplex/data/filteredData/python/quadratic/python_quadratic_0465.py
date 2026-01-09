def main(n):
    a = [(i % 7) + 1 for i in range(n)]
    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if x == 0:
                continue
            r = range(i % x, n, x)
            if s[i] == 0:
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                if any(a[j] > x and s[j] == 'B' for j in r):
                    if s[i] == 0:
                        m -= 1
                    s[i] = 'A'
    # print(''.join(s))
    pass
if __name__ == "__main__":
    main(10)