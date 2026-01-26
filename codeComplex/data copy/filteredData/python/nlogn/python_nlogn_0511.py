def main(n):
    from collections import defaultdict

    # Deterministic input generation
    # We interpret n as the length of the array l for a single test case.
    # To mimic varied values and some repetitions, we use a simple pattern.
    t = 1  # single test case
    test_cases = []
    for _ in range(t):
        length = max(1, n)
        # Generate an array with deterministic structure and repetitions
        # Values range between 1 and max(2, n//3) to create duplicates
        base = max(2, n // 3)
        l = [(i % base) + 1 for i in range(length)]
        test_cases.append((length, l))

    # Core logic from the original program
    for _ in range(t):
        n_case, l = test_cases[_]
        arr = defaultdict(lambda: 0)
        for i in l:
            arr[i] += 1

        values_with_at_least_two = []
        graterthan4 = 0
        isgraterthan4 = False
        for key in list(arr.keys()):
            if arr[key] >= 4:
                isgraterthan4 = True
                graterthan4 = key
            if arr[key] >= 2:
                values_with_at_least_two.append(key)

        values_with_at_least_two.sort()
        length_vals = len(values_with_at_least_two)

        if isgraterthan4:
            # print(graterthan4, graterthan4, graterthan4, graterthan4)
            pass

        else:
            # If we don't have at least two distinct values with count >= 2,
            # fall back to a deterministic placeholder based on available data
            if length_vals < 2:
                # Fallback: use first element repeated if available, else default to 1
                if values_with_at_least_two:
                    a = b = values_with_at_least_two[0]
                elif l:
                    a = b = l[0]

                else:
                    a = b = 1
                # print(a, a, b, b)
                pass

            else:
                m = 10**18
                mi = [values_with_at_least_two[0], values_with_at_least_two[1]]
                for i in range(length_vals - 1):
                    a = values_with_at_least_two[i]
                    b = values_with_at_least_two[i + 1]
                    val = a / b + b / a
                    if val < m:
                        m = val
                        mi = [a, b]
                a, b = mi
                # print(a, a, b, b)
                pass
if __name__ == "__main__":
    # Example call; adjust n to scale input size
    main(10)