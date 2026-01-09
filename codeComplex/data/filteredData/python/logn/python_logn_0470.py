def main(n):
    # n is ignored; the logic is fixed-size (bitwise search up to 2**29)
    # We simulate the interactive judge deterministically.
    # The hidden numbers a and b are generated deterministically from n.
    # Core idea: reuse the same querying pattern, but through a local judge.

    # Deterministically generate hidden a, b from n
    # Example: spread bits of n into a and b
    a_hidden = 0
    b_hidden = 0
    for i in range(30):
        if (n >> (2 * i)) & 1:
            a_hidden |= (1 << i)
        if (n >> (2 * i + 1)) & 1:
            b_hidden |= (1 << i)

    def judge(x, y):
        # Simulate original interactive answer:
        # compare (a^x) and (b^y):
        # if (a^x) > (b^y) => '1'
        # if (a^x) < (b^y) => '-1'
        # else '0'
        ax = a_hidden ^ x
        by = b_hidden ^ y
        if ax > by:
            return '1'
        elif ax < by:
            return '-1'

        else:
            return '0'

    # Simulated interactive I/O
    pending_query = None  # store last query parameters (x, y)

    def print_query(x, y):
        nonlocal pending_query
        pending_query = (x, y)

    def input_answer():
        nonlocal pending_query
        x, y = pending_query
        ans = judge(x, y)
        pending_query = None
        return ans

    # Original algorithm with replaced I/O
    print_query(0, 0)
    ans00 = input_answer()
    xr = 0
    a = 0
    b = 0
    cb = 2 ** 29
    while cb:
        print_query(xr + cb, cb)
        ans11 = input_answer()
        print_query(xr, cb)
        if ans11 == ans00:
            ans01 = input_answer()
            if ans01 == '1':
                a += cb
                b += cb

        else:
            ans00 = input_answer()
            if ans11 == '1':
                b += cb

            else:
                a += cb
            xr += cb
        cb //= 2
    # Output reconstructed a, b (the algorithm's result)
    # print("!", a, b)
    pass
    # Return them as well for programmatic use
    return a, b, a_hidden, b_hidden


if __name__ == "__main__":
    # Example deterministic call with n as input scale
    main(123456789)