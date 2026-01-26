def main(n):
    from collections import Counter

    # Interpret n as number of testcases
    testcase = max(1, n)

    # Deterministic data generation for A
    # For each testcase we need 2 lines: first is ignored in logic, second is used
    # We'll make each second line a list of integers whose size depends on n and t
    A = []
    for t in range(testcase):
        # First line for this testcase (unused by core algorithm)
        length1 = (t + 1) % 5 + 1
        line1 = [(i + 1) * (t + 2) for i in range(length1)]
        A.append(line1)

        # Second line for this testcase (used by algorithm)
        length2 = (t + 3) % 7 + n + 3  # ensure growth with n
        line2 = []
        base = t + 1
        for i in range(length2):
            # Deterministic pattern with repeated values to exercise logic
            # Mix of base, base+1, and base+2 with periodic repetition
            val = base + (i % 3)
            # Add more structure to allow potential >=4 and >=2 duplicates
            if i % 5 == 0:
                val = base
            elif i % 7 == 0:
                val = base + 1
            line2.append(val)
        A.append(line2)

    for t in range(testcase):
        counter = Counter(A[t * 2 + 1])
        LIST = []
        for c in counter:
            if counter[c] >= 4:
                # print(c, c, c, c)
                pass
                break
            elif counter[c] >= 2:
                LIST.append(c)

        else:
            LIST.sort()
            if len(LIST) < 2:
                # Degenerate case: not enough elements with count >= 2
                # Construct a deterministic fallback
                if len(LIST) == 0:
                    LIST = [1, 2]

                else:
                    LIST = [LIST[0], LIST[0] + 1]
            ANS = [LIST[0], LIST[1], LIST[1] / LIST[0]]
            for i in range(2, len(LIST)):
                ratio = LIST[i] / LIST[i - 1]
                if ratio < ANS[2]:
                    ANS = [LIST[i - 1], LIST[i], ratio]
            # print(ANS[0], ANS[0], ANS[1], ANS[1])
            pass
if __name__ == "__main__":
    main(10)