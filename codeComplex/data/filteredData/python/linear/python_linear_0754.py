def main(n):
    # Generate deterministic input array 'a' of length n
    # Example pattern: a[i] = (i % 7) - 3  → values in [-3, 3]
    a = [(i % 7) - 3 for i in range(n)]

    # Core logic from original program
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
    x = min(a)

    if len(a) % 2 == 1:
        for i in range(n):
            if a[i] == x:
                a[i] = -a[i] - 1
                break

    # Keep the original output behavior
    if a:
        # print(*a)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)