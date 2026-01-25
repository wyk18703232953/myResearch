def main(n):
    # Generate deterministic data based on n
    if n < 1:
        values = []
        queries = []
    else:
        # First part: original n elements
        base_n = n
        values = [i % 10 for i in range(base_n)]
        # Number of queries m grows with n (here m = n)
        m = n
        queries = []
        for i in range(m):
            # Deterministic query range within [1, base_n]
            l = (i % base_n) + 1
            r = base_n
            if l > r:
                l, r = r, l
            queries.append((l, r))

    # Core logic from original program
    cnt = 0
    length = len(values)
    for i in range(length):
        for j in range(i + 1, length):
            if values[i] > values[j]:
                cnt += 1

    from sys import stdout

    for l, r in queries:
        seg_n = r - l + 1
        cnt += seg_n * (seg_n - 1) // 2
        cnt &= 1
        if cnt == 1:
            stdout.write("odd\n")
        else:
            stdout.write("even\n")


if __name__ == "__main__":
    # Example deterministic call
    main(5)