def main(n):
    # Interpret n as number of nodes, ensure at least 2 to form a tree-like structure
    if n < 2:
        n = 2

    # Deterministic choice of s as a simple function of n
    s = n * (n + 1) // 2

    # Build a simple deterministic tree: a path 1-2-3-...-n
    degs = [0] * n
    for i in range(n - 1):
        a = i + 1
        b = i + 2
        degs[a - 1] += 1
        degs[b - 1] += 1

    leaf_count = degs.count(1)
    # Avoid division by zero; consistent behavior if no leaves exist
    if leaf_count == 0:
        result = 0
    else:
        result = 2 * s / leaf_count

    print(result)


if __name__ == "__main__":
    main(10)