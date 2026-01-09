def main(n):
    # n controls the length of arrays a and b
    if n <= 0:
        return

    # Deterministic generation of m, a, b
    m = n + 10
    # Ensure values sometimes equal 1 to trigger the -1 branch, but not always
    a = [(i % 5) + 1 for i in range(1, n + 1)]
    b = [((i * 2) % 5) + 1 for i in range(1, n + 1)]

    curr = float(m)
    f = 0

    if b[0] != 1:
        curr += curr / (b[0] - 1)

    else:
        f = 1

    for i in range(n - 1, -1, -1):
        if a[i] != 1:
            curr += curr / (a[i] - 1)

        else:
            f = 1
        if i > 0:
            if b[i] != 1:
                curr += curr / (b[i] - 1)

            else:
                f = 1

    if f:
        # print(-1)
        pass

    else:
        # print(curr - m)
        pass
if __name__ == "__main__":
    main(5)