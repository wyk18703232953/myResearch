import sys
from collections import defaultdict

def main(n):
    # Interpret n as both number of rows and number of columns
    # Ensure at least 1 row and 1 column
    if n <= 0:
        return
    rows = n
    cols = n

    # Deterministic generation of a matrix of size rows x cols
    # a[i][j] = (i * cols + j) % (2 * rows * cols)
    vals = defaultdict(list)
    elems = set()
    for i in range(rows):
        for pos in range(cols):
            v = (i * cols + pos) % (2 * rows * cols)
            elems.add(v)
            vals[v].append((pos, i))

    elems = sorted(elems, reverse=True)

    masks = [0] * rows
    full = (1 << cols) - 1
    met = {0: 0}
    for v in elems:
        for pos, i in vals[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # Found two rows whose masks are complementary
                # Output 1-based indices as in the original program
                print(i + 1, met[complement] + 1)
                return

    # If nothing found, mimic original behavior of not printing anything and exiting
    return

if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(8)