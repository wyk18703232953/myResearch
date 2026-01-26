def main(n):
    # Interpret n as the number of test cases and also as the size of each array
    t = n if n > 0 else 1
    results = []

    for case_idx in range(t):
        size = n if n > 0 else 1
        # Deterministically generate the array based on case index and size
        # Example pattern: a[i] = (case_idx + 1) * (i + 1)
        a = [(case_idx + 1) * (i + 1) for i in range(size)]

        if size == 1:
            results.append(0)

        else:
            max1 = max2 = -1
            for q in a:
                if q > max1:
                    max1, max2 = q, max1
                elif q > max2:
                    max2 = q
            results.append(max(0, min(max2 - 1, len(a) - 2)))

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # Example deterministic call
    main(5)