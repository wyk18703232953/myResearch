def main(n):
    # Interpret n as the length of the original input array b
    if n <= 0:
        return

    # Deterministic construction of b of length n
    # Example pattern: b[i] = (i + 1) * 3
    b = [(i + 1) * 3 for i in range(n)]

    a = [0] * (2 * len(b))
    a[-1] = b[0]
    for i in range(1, len(b)):
        if b[i] - a[i - 1] <= a[-i]:
            a[i] = a[i - 1]
            a[-i - 1] = b[i] - a[i - 1]

        else:
            a[-i - 1] = a[-i]
            a[i] = b[i] - a[-i - 1]
    # print(*a)
    pass
if __name__ == "__main__":
    main(10)