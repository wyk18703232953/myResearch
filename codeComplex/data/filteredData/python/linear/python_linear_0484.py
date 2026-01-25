def intersection(segs):
    end = float('inf')
    start = -float('inf')
    for l, r in segs:
        end = min(end, r)
        start = max(start, l)
    return start, end


def solve_from_segs(segs):
    starts = {}
    ends = {}
    x = intersection(segs)
    for l, r in segs:
        if r in starts:
            starts[r] = max(starts[r], l)
        else:
            starts[r] = l
        if l in ends:
            ends[l] = min(ends[l], r)
        else:
            ends[l] = r

    b = segs.copy()
    if (x[0], ends.get(x[0], x[0])) in b:
        b.remove((x[0], ends[x[0]]))
    y = intersection(b) if b else (0, 0)

    c = segs.copy()
    if (starts.get(x[1], x[1]), x[1]) in c:
        c.remove((starts[x[1]], x[1]))
    z = intersection(c) if c else (0, 0)

    return max(x[1] - x[0], y[1] - y[0], z[1] - z[0], 0)


def generate_segments(n):
    # Deterministically generate n segments:
    # i-th segment is (i, 2*i + (i % 3)) for i in range(n)
    segs = [(i, 2 * i + (i % 3)) for i in range(n)]
    return segs


def main(n):
    segs = generate_segments(n)
    result = solve_from_segs(segs)
    print(result)


if __name__ == "__main__":
    main(10)