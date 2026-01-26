def main(n):
    # Deterministic data generation
    # Ensure length is even and at least 2
    m = max(2, n if n % 2 == 0 else n + 1)

    # Generate a and b deterministically
    # a: increasing sequence, b: some deterministic pattern
    a = [i for i in range(1, m + 1)]
    b = [(i * 3) % 100 for i in range(1, m + 1)]

    # Core logic from original program
    a1 = min(a[::2])
    b1 = max(a[::2])
    c1 = min(a[1::2])
    d1 = max(a[1::2])
    g = sum(b[::2]) / 4
    h = sum(b[1::2]) / 4
    r = abs(b[0] - g) + abs(b[1] - h)

    found = False
    for i in range(a1, b1 + 1):
        for j in range(c1, d1 + 1):
            if abs(i - g) + abs(j - h) <= r:
                found = True
                break
        if found:
            break

    if found:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)