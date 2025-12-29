import random


def intersection(segs):
    end = float('inf')
    start = - float('inf')
    for l, r in segs:
        end = min(end, r)
        start = max(start, l)
    return start, end


def solve(segs):
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
    if (x[0], ends[x[0]]) in b:
        b.remove((x[0], ends[x[0]]))
    y = intersection(b)

    c = segs.copy()
    if (starts[x[1]], x[1]) in c:
        c.remove((starts[x[1]], x[1]))
    z = intersection(c)

    return max(x[1] - x[0], y[1] - y[0], z[1] - z[0], 0)


def gen_test_data(n):
    segs = []
    base_min = 0
    base_max = 10**6
    for _ in range(n):
        l = random.randint(base_min, base_max - 1)
        r = random.randint(l, base_max)
        segs.append((l, r))
    return segs


def main(n):
    segs = gen_test_data(n)
    return solve(segs)


if __name__ == "__main__":
    # 示例：n = 5
    print(main(5))