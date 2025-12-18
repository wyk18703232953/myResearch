import sys

input = sys.stdin.readline


def intersection(segs):
    end = float('inf')
    start = - float('inf')
    for l, r in segs:
        end = min(end, r)
        start = max(start, l)
    return start, end


def solve():
    n = int(input())
    segs = [tuple([int(x) for x in input().split(' ')]) for s in range(n)]
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
    b.remove((x[0], ends[x[0]]))
    y = intersection(b)

    c = segs.copy()
    c.remove((starts[x[1]], x[1]))
    z = intersection(c)

    return max(x[1] - x[0], y[1] - y[0], z[1] - z[0], 0)

print(solve())
