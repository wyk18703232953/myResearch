def main(n):
    # n: number of nodes in a tree
    # Generate a fixed tree and a fixed sum s deterministically based on n
    if n <= 1:
        # Handle trivial case: no edges, avoid division by zero
        s = 0
        print(0)
        return

    # Deterministically generate s as a simple function of n
    s = n * (n + 1) // 2

    # Initialize degree list
    l = [0 for _ in range(n)]

    # Deterministically generate a tree:
    # Connect node i with node (i % (i+1)) to ensure a tree-like structure.
    # To keep closer to common tree constructions, we'll just make a simple chain.
    # Edge i connects node i and i+1 (1-based indexing in original code).
    for i in range(n - 1):
        a = i + 1      # 1-based
        b = i + 2      # 1-based
        l[a - 1] += 1
        l[b - 1] += 1

    count = 0
    for i in range(n):
        if l[i] == 1:
            count += 1

    if count == 0:
        print(0)
    else:
        print((s / count) * 2)


if __name__ == "__main__":
    # Example call for testing with a chosen scale n
    main(10)