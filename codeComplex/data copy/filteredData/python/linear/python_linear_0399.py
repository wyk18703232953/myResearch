def main(n):
    # n controls the length of arrays a and b
    if n <= 0:
        return 0

    # Deterministic m based on n
    m = n * 10

    # Deterministic construction of arrays a and b, avoiding too many 1s to reduce -1 outputs
    # Ensure values are in a small positive range, some 1s may appear
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
        result = -1

    else:
        result = curr - m

    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example call for experimental scaling; adjust n as needed
    main(10)