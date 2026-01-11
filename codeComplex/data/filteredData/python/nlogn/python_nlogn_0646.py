def main(n):
    # Interpret n as the scale: number of vertical segments v and horizontal segments h
    # Generate deterministic input structure:
    # v = n, h = n
    v = n
    h = n

    # Generate vs: v integers in non-decreasing order
    # Example: vs[i] = i * 2 (already sorted, no duplicates needed)
    vs = [i * 2 for i in range(v)]
    vs.sort()
    vs.append(10 ** 9)

    # Generate hs: only those with x1 == 1 are kept in original program
    # Structure: [x1, x2, y], with x1 == 1
    # Make x2 roughly increasing but interleaved with vs to exercise the algorithm
    hs = []
    for i in range(h):
        x1 = 1
        x2 = i * 3 + 1
        y = i  # y is irrelevant for the algorithm
        if x1 == 1:
            hs.append([x1, x2, y])

    def sort_x2(val):
        return val[1]

    hs.sort(key=sort_x2)

    hsl = len(hs)
    vsl = len(vs)

    res = v + h
    hi = 0
    for vi, v_val in enumerate(vs, start=0):
        while hi < hsl and hs[hi][1] < v_val:
            hi += 1
        res = min(res, vi + hsl - hi)

    # print(res)
    pass
if __name__ == "__main__":
    # Example call for testing / timing
    main(1000)