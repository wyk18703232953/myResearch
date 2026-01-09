def main(n):
    # n controls the bit-length of hidden numbers a and b
    # Hidden numbers are deterministically generated from n
    a = (1 << n) - 1          # all bits 1 up to n
    b = ((1 << n) - 1) ^ (1 << (n // 2))  # same as a but one bit flipped

    c = 0
    d = 0

    def ask(c_local, d_local):
        nonlocal a, b
        # Original interactive comparator:
        # returns -1 if (a ^ c_local) < (b ^ d_local)
        # returns 1  if (a ^ c_local) > (b ^ d_local)
        # returns 0  otherwise
        ac = a ^ c_local
        bd = b ^ d_local
        if ac < bd:
            return -1
        elif ac > bd:
            return 1

        else:
            return 0

    def solve(mi, base):
        nonlocal c, d

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

    solve(n - 1, ask(0, 0))
    # Return c, d, a, b to allow verification in experiments
    return c, d, a, b


if __name__ == "__main__":
    # Example deterministic call for experiments; adjust n as needed
    result = main(30)
    # print(result)
    pass