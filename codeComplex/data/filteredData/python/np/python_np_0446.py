def main(n):
    from collections import defaultdict

    # Map n to matrix size: rows = n, columns = fixed m
    m = 8

    # Deterministic data generation
    vals = set()
    locs = defaultdict(list)
    for i in range(n):
        row = [((i * m + pos) % (2 * n + 5)) for pos in range(m)]
        for pos, v in enumerate(row):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * n
    full = (1 << m) - 1
    met = {0: 0}

    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # In original code, program exits after first output
                # We keep same behavior: return when found
                # Return 1-based indices to match original print
                return i + 1, met[complement] + 1

    # If no pair is found, return a deterministic default
    return -1, -1


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiment
    res = main(10**3)
    print(res)