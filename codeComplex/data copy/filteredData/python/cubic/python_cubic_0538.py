def main(n):
    # Deterministically generate inputs based on n
    # a_str: string of digits "0..(n-1)%10"
    a_str = "".join(str(i % 10) for i in range(n))
    # b: an integer with n+1 digits, all '9' (guaranteed >= any permutation of a_str)
    b = int("9" * (n + 1))

    a = sorted(a_str)
    a = a[::-1]  # reverse a
    p = ''
    cnt = [0] * 10  # kept from original, though unused

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
    main(5)