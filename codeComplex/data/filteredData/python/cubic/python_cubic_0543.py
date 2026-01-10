def main(n):
    # Deterministic data generation based on n
    # a_str is the string that would have been read from input()
    # b is the integer limit that would have been read from input()
    # We let length of a_str be n, and construct digits deterministically.
    a_str = ''.join(str((i * 7) % 10) for i in range(n))
    b = int(''.join(str((i * 3 + 1) % 10) for i in range(max(1, n))))

    # Original algorithm starts here
    a = ''.join(reversed(sorted(a_str)))
    r = ''
    while len(a) > 0:
        for i in range(len(a)):
            candidate = r + a[i] + ''.join(sorted(a[:i] + a[i + 1:]))
            if int(candidate) <= b:
                r += a[i]
                a = a[:i] + a[i + 1:]
                break

    print(r)


if __name__ == "__main__":
    main(10)