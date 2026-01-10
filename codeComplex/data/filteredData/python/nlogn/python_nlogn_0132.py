def main(n):
    # Interpret n as the length of arr
    # Generate deterministic a, b, c and arr
    if n <= 0:
        n = 1

    # Deterministic parameters based on n
    a = n + 3
    b = 2 * n + 5
    c = n // 2 + 1

    # Generate a deterministic array of length n
    # Example: arr[i] = (i * 3 + 1) % (2*n + 1) + 1 to keep positives
    arr = [((i * 3 + 1) % (2 * n + 1)) + 1 for i in range(n)]

    # Core logic from original program
    arr.sort()
    p = 0
    a -= 1
    while a >= 0 and c < b:
        c -= 1
        p += 1
        c += arr[a]
        a -= 1
    if c < b:
        print(-1)
    else:
        print(p)


if __name__ == "__main__":
    main(10)