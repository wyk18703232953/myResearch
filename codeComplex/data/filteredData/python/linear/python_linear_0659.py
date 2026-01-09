def main(n):
    # Scale parameter n will be used as number of nodes
    if n < 2:
        # No edges possible, define behavior deterministically
        # print(0.0)
        pass
        return

    # Deterministic definition of s based on n
    s = n * (n + 1) // 2

    # Generate a simple path/tree: 1-2-3-...-n
    degs = [0] * n
    for i in range(n - 1):
        a = i + 1
        b = i + 2
        degs[a - 1] += 1
        degs[b - 1] += 1

    leaf_count = degs.count(1)
    if leaf_count == 0:
        # print(0.0)
        pass

    else:
        # print(2 * s / leaf_count)
        pass
if __name__ == "__main__":
    main(10)