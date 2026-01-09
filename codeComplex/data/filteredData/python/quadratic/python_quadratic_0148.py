def main(n):
    # Generate deterministic parts data based on n
    # Original code reads 4 blocks, each with n lines of n digits (0/1)
    # Here we construct a simple deterministic pattern using i, j, and block index b
    parts = []
    for b in range(4):
        part = []
        for i in range(n):
            row = [((i + j + b) % 2) for j in range(n)]
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
    # Example call for complexity experiment
    main(10)