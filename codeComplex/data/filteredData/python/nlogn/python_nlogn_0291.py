def main(n):
    # Interpret n as total number of operations; split into two phases
    # Phase 1: build initial dictionary with n1 pairs
    # Phase 2: update dictionary with n2 pairs
    n1 = n // 2
    n2 = n - n1

    d = {}
    # Deterministic generation of first n1 pairs (a, x)
    # Use simple arithmetic so keys collide in a controlled way
    for i in range(n1):
        a = i % max(1, n1 // 3 + 1)
        x = (i * 2 + 3) % (n1 + 5)
        d[a] = x

    # Deterministic generation of next n2 pairs (b, y)
    for j in range(n2):
        b = (j * 3 + 1) % max(1, n1 // 2 + 1)
        y = (j * 5 + 7) % (n2 + 7)
        d[b] = max(d.get(b, 0), y)

    result = sum(d.values())
    print(result)
    return result


if __name__ == "__main__":
    main(10)