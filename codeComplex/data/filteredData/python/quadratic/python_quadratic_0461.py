def main(n):
    # Deterministically generate input of size n
    # a is a list of positive integers
    a = [(i % 7) + 1 for i in range(n)]

    b = [0] * n  # preserved but unused, to keep structure
    s = [0] * n
    m = n
    while m:
        for i, x in enumerate(a):
            if s[i] == 0:
                r = range(i % x, n, x)
                if all(a[j] <= x or s[j] == 'A' for j in r):
                    s[i] = 'B'
                    m -= 1
                    if m == 0:
                        break
                if any(a[j] > x and s[j] == 'B' for j in r):
                    # Only change if still unset, to mimic original loop semantics:
                    if s[i] == 0:
                        s[i] = 'A'
                        m -= 1
                        if m == 0:
                            break
    # print(''.join(s))
    pass
if __name__ == "__main__":
    main(10)