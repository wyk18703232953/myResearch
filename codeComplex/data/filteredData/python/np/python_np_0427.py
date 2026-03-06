def main(n):
    from collections import defaultdict

    # Scale parameters based on n
    m = 8
    rows = max(1, n)

    # Deterministic data generation
    # Generate a rows x m matrix of integers
    # Example pattern: a[i][j] = i * m + j
    vals = set()
    locs = defaultdict(list)
    for i in range(rows):
        row = [i * m + j for j in range(m)]
        for pos, v in enumerate(row):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * rows
    full = (1 << m) - 1
    met = {0: 0}
    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # For time-complexity experiments we keep the same output behavior
                print(i + 1, met[complement] + 1)
                return

    # If no pair found, still produce deterministic output
    print(-1, -1)


if __name__ == "__main__":
    # Example deterministic call for time complexity experimentation
    main(10)