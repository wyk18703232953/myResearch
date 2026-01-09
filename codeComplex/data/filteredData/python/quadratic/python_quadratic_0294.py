def main(n):
    # Deterministic data generation:
    # We create an array a of length 2*n.
    # Pairs are constructed in a controlled way so that the algorithm
    # has non-trivial behavior but is fully deterministic.
    # Pattern: for i in 0..n-1, we create two occurrences of value i,
    # then deterministically shuffle them by a fixed pattern.
    a = []
    for i in range(n):
        a.extend([i, i])
    # Deterministic reordering to create mismatches:
    # Swap elements at positions (2k, 2k+1) when k is odd.
    for k in range(1, n, 2):
        idx1 = 2 * k
        idx2 = 2 * k + 1
        a[idx1], a[idx2] = a[idx2], a[idx1]

    swaps = 0
    for i in range(0, 2 * n, 2):
        if a[i] == a[i + 1]:
            continue

        c = a[i]
        j = i + 2
        while c != a[j]:
            j += 1

        MIN = i + 1
        while j > MIN:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
            swaps += 1

    # print(swaps)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)