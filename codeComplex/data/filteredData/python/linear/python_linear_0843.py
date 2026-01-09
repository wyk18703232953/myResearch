def main(n):
    # Interpret n as number of test cases; each test case i has array length i+1
    t = n
    results = []
    for case_idx in range(t):
        size = case_idx + 1
        # Deterministically generate array: a[i] = (i * 2 + 3) % (size + 5) + 1
        a = [(i * 2 + 3) % (size + 5) + 1 for i in range(size)]
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
    # Output phase kept for completeness of original behavior
    for ans in results:
        # print(ans)
        pass
if __name__ == "__main__":
    main(5)