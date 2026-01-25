def main(n):
    # n controls both the array size and the number of queries
    # Ensure minimum size to keep logic valid (need at least 2 elements)
    if n < 2:
        n = 2

    # Deterministically construct a and q
    q = n
    a = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]

    M = max(a)
    i = 0
    x = a[0]
    L = []
    L1 = []
    L2 = []
    while x != M and i + 1 < n:
        L1.append(x)
        L2.append(a[i + 1])
        i = i + 1
        if x < a[i]:
            L.append(x)
            x = a[i]
        else:
            L.append(a[i])

    # If the loop ended early because of bounds, adjust i and x to be consistent
    if i >= n - 1:
        i = n - 2
        x = max(a)

    b = a[i + 1 :] + L

    # Deterministically generate queries; original queries were 1-based integers
    # We cycle through a simple pattern that covers small, medium, and large m
    queries = [(k * 3 + 1) for k in range(q)]

    for m in queries:
        # In the original code m is read from input each time and used directly
        if m <= i:
            print(str(L1[m - 1]) + " " + str(L2[m - 1]))
        else:
            # Guard for n-1 > 0 (always true since n >= 2)
            print(str(x) + " " + str(b[(m - i - 1) % (n - 1)]))


if __name__ == "__main__":
    # Example deterministic run
    main(10)