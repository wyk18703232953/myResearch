def main(n):
    # n controls both the number of test cases and the size parameters inside
    # t = number of test cases
    t = max(1, n // 3)

    results = []

    for case_idx in range(t):
        # Deterministically derive n_i and k_i from the global n and case index
        # Ensure 1 <= k_i <= n_i
        base = case_idx + 1
        n_i = max(1, (n % 1000) + base)  # keep sizes moderate but growing
        k_i = max(1, min(n_i, (base * 7 + n) % (n_i) + 1))

        # Deterministically generate string s of length n_i over 'R', 'G', 'B'
        chars = ['R', 'G', 'B']
        s = ''.join(chars[(i + base) % 3] for i in range(n_i))

        mini = n_i

        # Core algorithm from original code
        test = "RGB" * (k_i // 3 + 5)
        for i in range(n_i - k_i + 1):
            count = 0
            for j in range(k_i):
                if s[i + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        test = "GBR" * (k_i // 3 + 5)
        for i in range(n_i - k_i + 1):
            count = 0
            for j in range(k_i):
                if s[i + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        test = "BRG" * (k_i // 3 + 5)
        for i in range(n_i - k_i + 1):
            count = 0
            for j in range(k_i):
                if s[i + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        results.append(mini)

    # Output all results to keep side effects similar to original
    for ans in results:
        # print(ans)
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(1000)