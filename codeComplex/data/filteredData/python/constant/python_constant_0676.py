def main(n):
    # n is ignored; kept for interface compatibility and potential scaling control
    # Deterministic answer generator for the interactive oracle
    def oracle(x, y, a, b):
        if (a ^ x) > (b ^ y):
            return '1'

        else:
            return '0'

    # Deterministically generate a and b from n
    # Example: encode n into a and b in a reversible, deterministic way
    a = n
    b = (n * 3) ^ (n // 2)

    # Simulate the original interactive protocol deterministically
    ans00 = oracle(0, 0, a, b)
    xr = 0
    da = 0
    db = 0
    cb = 2 ** 29
    while cb:
        ans11 = oracle(xr + cb, cb, a, b)
        ans10 = oracle(xr, cb, a, b)
        if ans11 == ans00:
            ans01 = ans10
            if ans01 == '1':
                da += cb
                db += cb

        else:
            ans00 = ans10
            if ans11 == '1':
                db += cb

            else:
                da += cb
            xr += cb
        cb //= 2

    # For time-complexity experiments, we simply run the logic; printing is optional
    # but kept to match the original program's observable behavior.
    # print("!", da, db)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)