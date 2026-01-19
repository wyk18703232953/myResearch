import sys
from collections import defaultdict

def main(n):
    # Interpret n as number of rows; keep m fixed to preserve original logic shape
    m = 8
    n_rows = n if n > 0 else 1

    vals = set()
    locs = defaultdict(list)

    # Deterministic data generation:
    # value at row i, column pos is computed from (i, pos)
    # Ensure a wide spread of values while fully deterministic
    for i in range(n_rows):
        row_vals = [(i * 31 + pos * 17) % (n_rows * m + 7) for pos in range(m)]
        for pos, v in enumerate(row_vals):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * n_rows
    full = (1 << m) - 1
    met = {0: 0}

    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # For scalability experiments we avoid sys.exit() and just return
                print(i + 1, met[complement] + 1)
                return

    # If no pair found, print a deterministic fallback
    print(-1, -1)


if __name__ == "__main__":
    # Example deterministic call; adjust n for experiments
    main(10)