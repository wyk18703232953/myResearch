def main(n):
    from collections import defaultdict as dd

    # Deterministically construct T test cases.
    # Here we let T be min(n, something) for scaling; use T = max(1, n//5)
    T = max(1, n // 5)
    test_cases = []

    # For each test case, construct an array of length related to n and test index
    # to scale input size with n deterministically.
    for t in range(T):
        length = max(4, n + t)  # ensure at least length 4
        arr = []
        # Deterministic pattern: values derived from index and test index
        for i in range(length):
            # produce moderate range of repeated values to exercise algorithm
            val = (i // 2 + t) % max(2, n // 2 + 1)
            arr.append(val)
        test_cases.append(arr)

    outputs = []

    for l in test_cases:
        l1 = dd(int)
        a = 0
        for j in l:
            l1[j] += 1
            if l1[j] == 4:
                a = j
        if a:
            outputs.append((a, a, a, a))
        else:
            c = 0
            x = 0
            l2 = []
            for j in l1:
                if l1[j] >= 2:
                    l2.append(j)
            l2.sort()
            a = 0
            b = 0
            for j in l2:
                c += 1
                if c == 1:
                    a = j
                elif c == 2:
                    b = j
                else:
                    if x / j + j / x < a / b + b / a:
                        a, b = x, j
                x = j
            outputs.append((a, a, b, b))

    # For timing experiments, you may want to avoid printing.
    # Here we still print to preserve observable behavior.
    for o in outputs:
        print(*o)


if __name__ == "__main__":
    main(1000)