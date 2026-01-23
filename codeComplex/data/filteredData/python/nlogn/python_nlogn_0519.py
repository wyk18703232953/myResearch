import math

def main(n):
    # n: number of test cases; each test case size depends on its index
    t = n
    outputs = []

    for case_idx in range(t):
        # Define size of array for this test case; ensure at least 2
        size = max(2, case_idx + 2)

        # Construct a array deterministically with duplicates
        # Pattern: values repeat every 3 positions
        a = [(i // 2 + case_idx) % (size // 2 + 1) + 1 for i in range(size)]

        b = []
        res_a, res_b = 1, int(1e18)

        a = sorted(a)
        i = 0
        while i < size - 1:
            if a[i] == a[i + 1]:
                b.append(a[i])
                i += 1
            i += 1

        def p2s(x, y):
            return (x + y) ** 2 / (x * y)

        for i in range(len(b) - 1):
            if p2s(res_a, res_b) > p2s(b[i], b[i + 1]):
                res_a, res_b = b[i], b[i + 1]

        outputs.append((res_a, res_a, res_b, res_b))

    for o in outputs:
        print(*o)


if __name__ == "__main__":
    main(5)