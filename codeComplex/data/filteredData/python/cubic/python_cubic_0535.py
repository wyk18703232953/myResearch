def main(n):
    # Generate deterministic test data based on n
    # a_str length = n, digits pattern: (i * 7) % 10
    a_str = "".join(str((i * 7) % 10) for i in range(n))
    # b is an integer with n digits: repeating pattern 9,8,7,...
    b = int("".join(str(9 - (i % 10)) for i in range(n)))

    a = sorted(a_str)
    a = a[::-1]
    p = ''

    while a:
        for i, d in enumerate(a):
            candidate = p + d + "".join(sorted(a[:i] + a[i+1:]))
            if int(candidate) <= b:
                p += d
                a.pop(i)
                break

    # print(p)
    pass
if __name__ == "__main__":
    main(10)