def main(n):
    # n controls the number of bits we simulate (up to 29, as in original cb=2**29)
    max_bits = min(n, 29)
    if max_bits <= 0:
        # print("! 0 0")
        pass
        return

    # Deterministic construction of hidden a and b for simulation:
    # For example:
    #   a = sum of odd bits < max_bits
    #   b = sum of even bits < max_bits
    a_hidden = 0
    b_hidden = 0
    for i in range(max_bits):
        if i % 2 == 0:
            b_hidden |= (1 << i)

        else:
            a_hidden |= (1 << i)

    # Query simulator: returns '1' if (x & y) != 0 else '0'
    def query(x, y):
        val = (a_hidden & x) ^ (b_hidden & y)
        return '1' if val != 0 else '0'

    # Original logic with queries replaced by deterministic simulator
    ans00 = query(0, 0)
    xr = 0
    a = 0
    b = 0
    cb = 2 ** max_bits // 2  # highest bit under max_bits

    while cb:
        ans11 = query(xr + cb, cb)
        _ = query(xr, cb)  # this call was present in original code but its return unused

        if ans11 == ans00:
            ans01 = query(xr, cb)
            if ans01 == '1':
                a += cb
                b += cb

        else:
            ans00 = query(xr, cb)
            if ans11 == '1':
                b += cb

            else:
                a += cb
            xr += cb
        cb //= 2

    # print("!", a, b)
    pass
if __name__ == "__main__":
    main(29)