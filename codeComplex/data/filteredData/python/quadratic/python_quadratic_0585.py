def main(n):
    # Interpret n as: number of test cases t = n,
    # and for each test case, string length and k both proportional to n.
    # This makes total work scale roughly with n^3 (t * n * k).
    t = n
    results = []
    for case_id in range(t):
        length = n
        k = max(1, n // 2)
        # Deterministically generate a string of length `length`
        # using a repeating "RGB" pattern shifted by case_id mod 3
        base = "RGB"
        shift = case_id % 3
        s_chars = []
        for i in range(length):
            s_chars.append(base[(i + shift) % 3])
        s = "".join(s_chars)

        mini = length

        test = "RGB" * (k // 3 + 5)
        for i in range(length - k + 1):
            count = 0
            for j in range(k):
                if s[i + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        test = "GBR" * (k // 3 + 5)
        for i in range(length - k + 1):
            count = 0
            for j in range(k):
                if s[i + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        test = "BRG" * (k // 3 + 5)
        for i in range(length - k + 1):
            count = 0
            for j in range(k):
                if s[i + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        results.append(str(mini))

    # print("\n".join(results))
    pass
if __name__ == "__main__":
    main(10)