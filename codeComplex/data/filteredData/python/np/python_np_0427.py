import sys
from collections import defaultdict

def main(n):
    # Interpret n as: number of rows; number of columns m is fixed and small
    m = 8
    n = max(1, int(n))

    # Deterministic data generation:
    # value at row i, column j is i * m + j
    vals = set()
    locs = defaultdict(list)
    for i in range(n):
        row_values = [i * m + j for j in range(m)]
        for pos, v in enumerate(row_values):
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
                print(i + 1, met[complement] + 1)
                return

if __name__ == "__main__":
    main(10)