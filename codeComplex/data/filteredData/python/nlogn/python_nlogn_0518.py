def process(A):
    d = {}
    final = set([])
    for x in A:
        if x not in d:
            d[x] = 0
        d[x] += 1
        if d[x] >= 4:
            return [x, x, x, x]
        if d[x] >= 2:
            final.add(x)
    L = sorted(final)
    answer = [float('inf'), None, None]
    for i in range(len(L) - 1):
        a = L[i]
        b = L[i + 1]
        a1 = a / b + b / a
        answer = min(answer, [a1, a, b])
    a1, a, b = answer
    return [a, a, b, b]


def main(n):
    # n controls both number of test cases and size per test case
    t = max(1, n)  # number of test cases
    base_len = max(1, n)  # length of each array

    results = []
    for ti in range(t):
        # deterministic generation of A for each test case
        length = base_len
        A = [(ti + 1) * (i % (n // 2 + 1) + 1) for i in range(length)]
        a, b, c, d = process(A)
        results.append((a, b, c, d))

    # print results to keep same observable behavior
    for a, b, c, d in results:
        print(f"{a} {b} {c} {d}")


if __name__ == "__main__":
    main(10)