def main(n):
    # Generate deterministic data based on n
    # Interpret n as both the size of the array and number of queries
    size = max(1, n)

    # Generate array l of length size: l[i] = (i * 2 + 1)
    l = [(i * 2 + 1) for i in range(size)]

    # Compute initial odd parity based on original inversion-like condition
    odd = 0
    for i in range(size):
        for j in range(i, size):
            if l[i] > l[j]:
                odd ^= 1

    # Number of queries m
    m = size
    ans = []

    # Generate deterministic queries:
    # ll and r are 1-based indices with 1 <= ll <= r <= size
    # Example pattern: ll = i % size + 1, r = size
    for i in range(m):
        ll = (i % size) + 1
        r = size
        k = r - ll + 1
        if (k * (k - 1) // 2) % 2:
            odd ^= 1
        ans.append("odd" if odd else "even")

    # print("\n".join(ans))
    pass
if __name__ == "__main__":
    main(10)