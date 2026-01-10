def main(n):
    # Ensure n is at least 1 to avoid empty behavior
    if n <= 0:
        print(0)
        return

    # Define sizes for the two phases based on n
    # First phase: n entries
    # Second phase: n entries
    n1 = n
    n2 = n

    d = {}

    # Deterministic generation for first batch of (a, x) pairs
    # Example: a cycles through 0..(n//2), x is a simple function of i
    for i in range(n1):
        a = i % max(1, (n // 2 + 1))
        x = i * 2 + 1
        if a in d:
            d[a][0] += 1
            d[a][1].append(x)
        else:
            d[a] = [1, [x]]

    # Deterministic generation for second batch of (a, x) pairs
    # Example: a offset and wrapped, x another simple function
    for i in range(n2):
        a = (i + n1 // 3) % max(1, (n // 2 + 1))
        x = i * 3 + 2
        if a in d:
            d[a][0] += 1
            d[a][1].append(x)
        else:
            d[a] = [1, [x]]

    s = 0
    for key in d:
        if d[key][0] == 1:
            s += d[key][1][0]
        else:
            s += max(d[key][1])
    print(s)


if __name__ == "__main__":
    main(10)