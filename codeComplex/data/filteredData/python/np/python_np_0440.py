def main(n):
    from collections import defaultdict

    # Determine matrix dimensions based on n
    # Let number of rows = n, number of columns = max(1, n % 20 + 1) (bounded to keep bitmasks reasonable)
    rows = n
    m = max(1, n % 20 + 1)

    # Deterministic generation of matrix values:
    # n rows, each with m integers
    # v(i, j) = (i * 131 + j * 17) % (2 * m)
    vals = set()
    locs = defaultdict(list)

    for i in range(rows):
        row_vals = [(i * 131 + j * 17) % (2 * m) for j in range(m)]
        for pos, v in enumerate(row_vals):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * rows
    full = (1 << m) - 1
    met = {0: 0}

    # Core logic preserved
    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # Found a pair of rows (1-based indices) whose bitmasks are complements
                return (i + 1, met[complement] + 1)

    # If no pair found, return a deterministic sentinel
    return (-1, -1)


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    res = main(1000)
    print(res)