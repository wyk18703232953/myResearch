def main(n):
    # Interpret n as: number of test cases t = n, each with string length and k derived deterministically
    t = n if n > 0 else 1

    results = []

    for case_idx in range(t):
        # Deterministically derive n_i and k_i for each test case based on case index
        # Keep them reasonable but scalable with n to allow time complexity experiments
        length = max(1, 5 * (case_idx + 1))     # string length
        k = max(1, (case_idx % length) + 1)     # window size, 1 <= k <= length

        # Generate a deterministic RGB string of given length
        base = "RGB"
        s = "".join(base[i % 3] for i in range(length))

        # Core algorithm logic from original program
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

        results.append(mini)

    # Output results, one per line, to mimic original program behavior
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for experiments
    main(3)