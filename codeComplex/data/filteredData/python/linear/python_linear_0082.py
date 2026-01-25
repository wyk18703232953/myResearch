def main(n):
    # Deterministic generation of input:
    # Original input structure:
    #   n
    #   n lines: x y
    #
    # Here, for a given n, we generate n pairs (x, y) deterministically.
    # We ensure x are strictly increasing so that sorting keeps the order.
    a = []
    for i in range(n):
        x = i * 2 + 1           # strictly increasing positions: 1,3,5,...
        y = (i * 3) % (n + 1) + 1  # power in [1, n+1], deterministic
        a.append([x, y])

    mem = [1]
    pos = []
    power = []

    # Equivalent to: a = sorted(rints_2d(n))
    a.sort()

    for x, y in a:
        pos.append(x)
        power.append(y)

    from bisect import bisect_left

    for i in range(1, n):
        ix = bisect_left(pos, pos[i] - power[i]) - 1
        if ix == -1:
            mem.append(1)
        else:
            mem.append(mem[ix] + 1)

    result = n - max(mem)
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)