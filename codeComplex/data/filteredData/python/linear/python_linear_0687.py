def main(n):
    # Ensure n is at least 2 and even to match the original center-splitting logic
    if n < 2:
        n = 2
    if n % 2 == 1:
        n += 1

    # Deterministic construction of b based on n
    # Example: b[i] = (i + 1) * 2
    b = [(i + 1) * 2 for i in range(n)]
    a = [0] * n

    l = n // 2 - 1
    r = n // 2

    a[l] = b[l] // 2
    a[r] = b[l] - a[l]

    while l > 0:
        if b[l - 1] >= b[l]:
            a[l - 1] = a[l]
            a[r + 1] = b[l - 1] - a[l]
        else:
            a[r + 1] = a[r]
            a[l - 1] = b[l - 1] - a[r]
        l -= 1
        r += 1

    print(*a)


if __name__ == "__main__":
    main(10)