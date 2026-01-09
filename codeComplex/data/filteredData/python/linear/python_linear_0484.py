def intersection(segs):
    end = float('inf')
    start = -float('inf')
    for l, r in segs:
        end = min(end, r)
        start = max(start, l)
    return start, end


def solve(segs):
    n = len(segs)
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
    rem1 = (x[0], ends.get(x[0], x[0]))
    if rem1 in b:
        b.remove(rem1)
    y = intersection(b) if b else (0, 0)

    c = segs.copy()
    rem2 = (starts.get(x[1], x[1]), x[1])
    if rem2 in c:
        c.remove(rem2)
    z = intersection(c) if c else (0, 0)

    return max(x[1] - x[0], y[1] - y[0], z[1] - z[0], 0)


def generate_segments(n):
    segs = []
    for i in range(n):
        l = i
        r = i + (i % 5) + 1
        segs.append((l, r))
    return segs


def main(n):
    segs = generate_segments(n)
    result = solve(segs)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)