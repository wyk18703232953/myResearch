def main(n):
    # Ensure n is at least 2 to avoid negative ranges
    if n < 2:
        n = 2

    # Deterministic generation of a and b based on n
    # a and b are lists of characters
    a = [('0' if i % 2 == 0 else '1') for i in range(n)]
    b = [('1' if (i // 2) % 2 == 0 else '0') for i in range(n)]

    ans = 0

    for i in range(n - 1):
        if a[i] == b[i]:
            continue
        if a[i + 1] == b[i + 1]:
            continue

        if a[i] == b[i + 1] and a[i + 1] == b[i]:
            a[i], a[i + 1] = a[i + 1], a[i]
            ans += 1

    for i in range(n):
        ans += (a[i] != b[i])

    print(ans)


if __name__ == "__main__":
    main(10)