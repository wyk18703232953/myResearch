def main(n):
    # Deterministically generate input string a and integer b based on n
    # a will be a string of digits with length n, cycling through '0'-'9'
    a_str = "".join(str(i % 10) for i in range(n))
    b = int("9" * max(1, n // 2))

    a = sorted(a_str)
    a = a[::-1]  # reverse a
    p = ''
    cnt = [0] * 10  # kept to preserve original structure, though unused

    while a:
        for i, d in enumerate(a):
            n_str = p + d + "".join(sorted(a[:i] + a[i + 1:]))
            if int(n_str) <= b:
                p += d
                a.pop(i)
                break

    # print(p)
    pass
if __name__ == "__main__":
    main(10)