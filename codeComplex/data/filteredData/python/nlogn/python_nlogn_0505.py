def main(n):
    # Interpret n as the number of entries; m is derived deterministically from n
    # Generate deterministic (x, y) pairs similar to arbitrary input
    # Ensure non-trivial behavior by mixing values
    m = n * (n // 2)  # capacity derived from n

    entries = []
    for i in range(1, n + 1):
        a = i * 3        # base value
        b = i % 5 - 2    # can be negative, small adjustments
        entries.append((a, b))

    # Core logic from original program
    entries.sort(key=lambda x: x[1] - x[0])

    size = sum(x[0] for x in entries)
    count = 0

    while size > m and count < n:
        size -= entries[count][0] - entries[count][1]
        count += 1

    result = -1 if size > m else count
    # print(result)
    pass
if __name__ == "__main__":
    main(10)