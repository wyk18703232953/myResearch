def main(n):
    # Deterministically generate input array a of length n
    # Example: a[i] = (i * 2 + 1) % (2 * n) + 1
    a = [((i * 2 + 1) % (2 * n)) + 1 for i in range(n)]

    b = [0] * n
    for i in range(n):
        if (i + 1 > a[i]):
            b[i] = i + 1

        else:
            q = (a[i] - (i + 1) + n) // n
            b[i] = i + 1 + q * n
    result = b.index(min(b)) + 1
    return result


if __name__ == "__main__":
    # Example: run main with a chosen input scale
    n = 10
    # print(main(n))
    pass