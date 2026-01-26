from bisect import bisect_left

def main(n):
    # Interpret n as total number of segments: roughly half vertical, half horizontal
    if n < 2:
        n = 2
    v_count = n // 2
    h_total = n - v_count

    # Generate deterministic vertical positions
    verticals = [2 * i + 1 for i in range(v_count)]

    # Generate deterministic horizontal segments data h as pairs (type, coord)
    # type 1 contributes to horizontals; type 0 is ignored later
    h = []
    for i in range(h_total):
        t = 1 if i % 2 == 0 else 0
        coord = 3 * i + 2
        h.append((t, coord))

    horizontals = [t[1] for t in h if t[0] == 1]

    verticals.sort()
    horizontals.sort()
    verticals.append(10**9)
    min_blockers = v_count + h_total
    for i, v in enumerate(verticals):
        cur_blockers = len(horizontals) - bisect_left(horizontals, v) + i
        if cur_blockers < min_blockers:
            min_blockers = cur_blockers

    # print(min_blockers)
    pass
if __name__ == "__main__":
    main(1000)