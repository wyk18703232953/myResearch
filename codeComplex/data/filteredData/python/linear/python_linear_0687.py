def main(n):
    if n < 2:
        return []

    # Ensure even n as required by the original logic (n//2 - 1 and n//2 must be valid and form pairs)
    if n % 2 == 1:
        n -= 1
        if n < 2:
            return []

    # Deterministically generate b of length n
    # Example pattern: b[i] = (i + 1) * 3
    b = [(i + 1) * 3 for i in range(n)]
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

    # print(*a)
    pass
    return a


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)