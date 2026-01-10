def main(n):
    # Interpret n as:
    # total numbers = n
    # k = n // 3 (non-zero scaling)
    k = max(1, n // 3)

    # Deterministically generate array a of length n
    # Pattern: a[i] = (i * 2) % (3 * k + 1)
    a = [(i * 2) % (3 * k + 1) for i in range(n)]

    # Core logic from original program
    current_n = n  # use a separate variable to preserve input n
    a_sorted, j = sorted(a), 0
    for i in a_sorted:
        while j < len(a_sorted) and i > a_sorted[j]:
            if i <= a_sorted[j] + k:
                current_n -= 1
            j += 1

    print(current_n)


if __name__ == "__main__":
    # Example deterministic call
    main(10)