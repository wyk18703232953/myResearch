def main(n):
    t = n
    results = []
    for case_id in range(1, t + 1):
        size = case_id
        a = []
        for i in range(size):
            a.append((i * i + case_id) % (size + 5) + 1)

        b = []
        res_a, res_b = 1, 10**18

        a = sorted(a)
        i = 0
        while i < size - 1:
            if a[i] == a[i + 1]:
                b.append(a[i])
                i += 1
            i += 1

        p2s = lambda x, y: (x + y) ** 2 / (x * y) if x != 0 and y != 0 else float('inf')

        for i in range(len(b) - 1):
            if p2s(res_a, res_b) > p2s(b[i], b[i + 1]):
                res_a, res_b = b[i], b[i + 1]

        results.append((res_a, res_a, res_b, res_b))

    for res in results:
        print(*res)


if __name__ == "__main__":
    main(5)