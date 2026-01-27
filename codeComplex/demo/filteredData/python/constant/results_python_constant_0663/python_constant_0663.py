def main(n):
    # Interpret n as the bit-length of the hidden numbers a and b
    # Deterministically construct hidden a, b from n
    # Example: use simple patterns based on n for reproducibility
    global a, b, c, d

    # Hidden values construction (deterministic, scalable)
    # a: bits at positions where i % 2 == 0
    # b: bits at positions where i % 3 == 0
    a = 0
    b = 0
    for i in range(n):
        if i % 2 == 0:
            a |= (1 << i)
        if i % 3 == 0:
            b |= (1 << i)

    c = 0
    d = 0

    def ask(c_local, d_local):
        # Simulate the original interactive judge deterministically.
        # The original problem is the classic AtCoder interactive task:
        # ask(c, d) returns:
        #   -1 if (a ^ c) < (b ^ d)
        #    0 if (a ^ c) == (b ^ d)
        #    1 if (a ^ c) > (b ^ d)
        ac = a ^ c_local
        bd = b ^ d_local
        if ac < bd:
            return -1
        elif ac > bd:
            return 1

        else:
            return 0

    def solve(mi, base):
        def solve_same():
            nonlocal c, d
            for i in range(mi, -1, -1):
                bit = 1 << i
                res1 = ask(c ^ bit, d)
                res2 = ask(c, d ^ bit)
                if res1 == -1 and res2 == 1:
                    c |= bit
                    d |= bit

        def solve1():
            nonlocal c, d
            for i in range(mi, -1, -1):
                bit = 1 << i
                res1 = ask(c ^ bit, d ^ bit)
                if res1 == -1:
                    c |= bit
                    return solve(i - 1, ask(c, d))

                else:
                    res2 = ask(c ^ bit, d)
                    if res2 == -1:
                        c |= bit
                        d |= bit

        def solve2():
            nonlocal c, d
            for i in range(mi, -1, -1):
                bit = 1 << i
                res1 = ask(c ^ bit, d ^ bit)
                if res1 == 1:
                    d |= bit
                    return solve(i - 1, ask(c, d))

                else:
                    res2 = ask(c, d ^ bit)
                    if res2 == 1:
                        c |= bit
                        d |= bit

        if base == 0:
            solve_same()
        elif base == 1:
            solve1()

        else:
            solve2()

    # Run the algorithm on bit positions [0..n-1]
    solve(n - 1, ask(0, 0))

    # Return (c, d) so that external code can verify correctness or measure time
    return c, d, a, b


if __name__ == "__main__":
    # Example deterministic call; change n to scale input size
    n = 30
    c, d, a, b = main(n)
    # print(c, d, a, b)
    pass