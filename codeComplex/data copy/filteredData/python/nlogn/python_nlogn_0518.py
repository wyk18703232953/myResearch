def process(A):
    d = {}
    final = set()
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
        if a1 < answer[0]:
            answer = [a1, a, b]
    _, a, b = answer
    return [a, a, b, b]


def build_test_case(n, case_index):
    length = max(4, n)
    A = []
    for i in range(length):
        val = (i + 1) + (case_index + 1)
        if val % 5 == 0:
            val = val // 2
        A.append(val)
    return A


def main(n):
    t = max(1, n)
    results = []
    for case_index in range(t):
        A = build_test_case(n, case_index)
        a, b, c, d = process(A)
        results.append((a, b, c, d))
    for a, b, c, d in results:
        print(f"{a} {b} {c} {d}")


if __name__ == "__main__":
    main(5)