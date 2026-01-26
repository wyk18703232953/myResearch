def main(n):
    # Generate 4 parts, each an n x n matrix of digits (0 or 1).
    # Here we deterministically generate them using simple arithmetic patterns.
    parts = []
    for p in range(4):
        part = []
        for i in range(n):
            row = []
            for j in range(n):
                # Deterministic pattern depending on part index, row, and column
                val = (i + j + p) % 2
                row.append(val)
            part.append(row)
        parts.append(part)

    processed_parts = []
    for part in parts:
        dt1 = 0
        exp = 1

        for h in range(n):
            for w in range(n):
                if part[h][w] != exp:
                    dt1 += 1
                exp = (exp + 1) % 2

        dt2 = 0
        for h in range(n):
            for w in range(n):
                if part[h][w] != exp:
                    dt2 += 1
                exp = (exp + 1) % 2

        processed_parts.append([dt1, dt2])

    ans = n * n * 4

    for i in range(3):
        for j in range(i + 1, 4):
            a = 0
            for k, part in enumerate(processed_parts):
                if k == i or k == j:
                    a += part[0]

                else:
                    a += part[1]
            ans = min(ans, a)

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call for experimental purposes
    main(5)