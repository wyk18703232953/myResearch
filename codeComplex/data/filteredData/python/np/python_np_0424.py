import sys
from collections import defaultdict

def main(n):
    # n controls the number of rows; keep m fixed (same role as original input)
    if n <= 0:
        return

    # choose a deterministic column count
    m = 8
    # full mask over m bits
    full = (1 << m) - 1

    # deterministic value generator:
    # val(i, j) = (i * (m + 1) + j * 7) % (2 * n + 3)
    def gen_value(i, j):
        return (i * (m + 1) + j * 7) % (2 * n + 3)

    vals = set()
    locs = defaultdict(list)

    # build deterministic "input matrix" of size n x m
    for i in range(n):
        row = [gen_value(i, j) for j in range(m)]
        for pos, v in enumerate(row):
            vals.add(v)
            locs[v].append((pos, i))

    masks = [0] * n
    met = {0: 0}

    for v in sorted(vals, reverse=True):
        for pos, i in locs[v]:
            curr_mask = masks[i] = masks[i] | (1 << pos)
            met[curr_mask] = i
            complement = full ^ curr_mask
            if complement in met:
                # identical behavior: print 1-based indices and return
                print(i + 1, met[complement] + 1)
                return

    # if nothing found, mimic "no output then exit"
    return


if __name__ == "__main__":
    # example call; adjust n as needed for experiments
    main(10)