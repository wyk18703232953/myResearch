import sys
from collections import defaultdict

def main(n):
    # Interpret n as both the number of rows and the number of columns
    # Ensure m is at most n and at least 1
    m = max(1, min(n, 20))
    n_rows = n

    # Deterministically generate matrix values:
    # value at (i, pos) is (i * m + pos) % (2 * m)
    elems = set()
    vals = defaultdict(list)
    for i in range(n_rows):
        row = [(i * m + pos) % (2 * m) for pos in range(m)]
        for pos, v in enumerate(row):
            elems.add(v)
            vals[v].append((pos, i))

    elems = sorted(elems, reverse=True)

    masks = [0] * n_rows
    full = (1 << m) - 1
    met = {0: 0}

    for v in elems:
        for pos, i in vals[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # Instead of exiting the process, just print and return to keep it reusable
                print(i + 1, met[complement] + 1)
                return

    # If no pair is found, print a deterministic default
    print(-1, -1)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)