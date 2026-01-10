def main(n):
    t = n
    results = []
    for case_idx in range(t):
        # Define size of array for this test case deterministically
        m = n + case_idx
        # Generate a deterministic array with repeated elements to ensure pairs exist
        a = [(i % (n // 2 + 1)) + 1 for i in range(m)]
        b = []
        res_a, res_b = 1, 10**18

        a = sorted(a)
        i = 0
        while i < m - 1:
            if a[i] == a[i + 1]:
                b.append(a[i])
                i += 1
            i += 1

        def p2s(x, y):
            return (x + y) ** 2 / (x * y)

        for i in range(len(b) - 1):
            if p2s(res_a, res_b) > p2s(b[i], b[i + 1]):
                res_a, res_b = b[i], b[i + 1]

        results.append((res_a, res_a, res_b, res_b))

    for r in results:
        print(*r)


if __name__ == "__main__":
    main(5)