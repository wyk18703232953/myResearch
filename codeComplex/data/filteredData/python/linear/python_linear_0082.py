def main(n):
    mem = [1]
    pos = []
    power = []

    # Deterministically generate n pairs (x, y)
    # Ensure x is non-decreasing after sort and power > 0
    a = []
    for i in range(n):
        x = i * 2
        y = (i % 5) + 1
        a.append([x, y])

    a.sort()

    for x, y in a:
        pos.append(x)
        power.append(y)

    for i in range(1, n):
        # manual bisect_left to avoid extra imports
        target = pos[i] - power[i]
        lo, hi = 0, i
        while lo < hi:
            mid = (lo + hi) // 2
            if pos[mid] < target:
                lo = mid + 1

            else:
                hi = mid
        ix = lo - 1

        if ix == -1:
            mem.append(1)

        else:
            mem.append(mem[ix] + 1)

    result = n - max(mem)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)