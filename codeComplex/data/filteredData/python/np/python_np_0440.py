import sys
from collections import defaultdict

def main(n):
    # Interpret n as both number of rows and number of columns
    # Ensure at least 1 row and 1 column
    if n <= 0:
        return

    m = n
    n_rows = n

    vals = set()
    locs = defaultdict(list)

    # Deterministic data generation:
    # grid[i][pos] = (i * m + pos) % (2 * m)
    for i in range(n_rows):
        curr_row = []
        for pos in range(m):
            v = (i * m + pos) % (2 * m)
            curr_row.append(v)
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
                # Keep the same observable behavior: print and exit
                print(i + 1, met[complement] + 1)
                return

if __name__ == "__main__":
    # Example deterministic call
    main(8)