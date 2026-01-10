def main(n):
    # Interpret n as both number of x-elements and number of segments m
    # Deterministic data generation

    # Generate n x-values in non-decreasing order
    # Example pattern: x[i] = i * 2
    x = [i * 2 for i in range(n)]
    m = n

    # Simulate segment inputs (x1, x2, y)
    # We only care about those with x1 == 1, so construct some deterministically
    vert = []
    for i in range(m):
        # Make every second segment have x1 == 1
        if i % 2 == 0:
            x1 = 1
        else:
            x1 = 2
        x2 = i + 1
        y = i  # unused, but kept for structural similarity
        if x1 == 1:
            vert.append(x2)

    # Append sentinel to x as in original code
    x.append(1000000000)

    # Core logic preserved
    vert.sort()
    x.sort()
    cur = 0
    minicount = n + m
    k = len(vert)
    for i in range(n + 1):
        while cur < k:
            if x[i] <= vert[cur]:
                break
            cur += 1
        minicount = min(minicount, k - cur + i)

    # For timing experiments, we just print the result
    print(minicount)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)