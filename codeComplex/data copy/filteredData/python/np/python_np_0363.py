def main(n):
    # n: number of test cases; each test case size grows with index
    q = max(1, n)
    results = []

    for tcase in range(1, q + 1):
        # Deterministically define c, r from test case index and n
        c = max(1, (tcase % 7) + (n % 5) + 1)  # number of rows in original input
        r = max(1, (tcase % 5) + (n % 3) + 1)  # number of columns in original input

        # Limit sizes so runtime is reasonable but still grows with n
        c = min(c + n // 3, 10 + n // 2)
        r = min(r + n // 4, 8 + n // 2)

        # Generate deterministic matrix "matt" of size c x r
        # Original program: c lines, each with r integers
        matt = [[(i * r + j + tcase + n) % 1000 for j in range(r)] for i in range(c)]

        # Transpose to get mat[r][c]
        mat = [[matt[i][j] for i in range(c)] for j in range(r)]

        # Append max of each row, then reverse each row
        for i in range(r):
            mat[i].append(max(mat[i]))
            mat[i].reverse()

        # Sort rows, then reverse order (descending lexicographically)
        mat.sort()
        mat.reverse()

        # Take up to first 4 rows as "work"
        work = mat[:min(4, r)]
        for t in work:
            t.pop(0)
        r_eff = min(4, r)

        wyn = 0
        # Enumerate all combinations of shifts: c**r_eff possibilities
        for num in range(c ** r_eff):
            shif = [(num // (c ** i)) % c for i in range(r_eff)]
            new = 0
            for i in range(c):
                kol = [work[j][(i + shif[j]) % c] for j in range(r_eff)]
                new += max(kol)
            wyn = max(wyn, new)

        results.append(wyn)

    # For experimental usage, print all results
    for v in results:
        print(v)


if __name__ == "__main__":
    main(5)