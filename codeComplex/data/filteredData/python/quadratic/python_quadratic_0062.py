def main(n):
    # n controls the size of the array w and number of queries m
    if n <= 0:
        return

    # Deterministic generation of w: values in [0, n)
    w = [i % n for i in range(n)]

    # Let number of queries m be n as well for scalability
    m = n

    # Core algorithm: compute initial inversion parity
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if w[i] > w[j]:
                c += 1
    c %= 2

    # Deterministic generation of queries (l, r)
    # We'll generate intervals with simple patterns depending on n
    results = []
    for j in range(m):
        # Example pattern:
        # l cycles from 1 to n, r is l plus an offset within bounds
        l = (j % n) + 1
        length = (j // 2) % n + 1  # length in [1, n]
        r = l + length - 1
        if r > n:
            r = n

        x = r - l + 1
        if x != 1 and (x * (x - 1) // 2) % 2:
            c = not c
        if c:
            results.append("odd")

        else:
            results.append("even")

    # Output results line by line to match original behavior
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(10)