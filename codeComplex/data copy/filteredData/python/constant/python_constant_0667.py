def main(n):
    # We simulate an interactive oracle.
    # Original interaction:
    # print("? x y"); ans = input()
    # Meaning inferred: for given hidden a,b, responses depend on comparisons.
    # Here we choose deterministic a,b based on n, then define answer(x,y).
    #
    # The original interactive solution is for the classic problem:
    # Given the answers for comparisons of (a^b) vs ( (a+x) ^ (b+y) ) etc.
    # However, the exact protocol isn't explicit from the snippet alone.
    # We reconstruct behavior consistent with the decision branches:
    #
    # The algorithm maintains:
    #   xr  = a ^ b  (unknown to the program, but simulated in oracle)
    # and in each step tests two queries with (xr+cb, cb) and (xr, cb).
    #
    # To keep the *control flow* and bit decisions identical, we only need:
    # - Three-valued comparison pattern that makes the branches well-defined.
    # We choose hidden a,b and define the oracle according to the well-known
    # Codeforces problem "Game of Bits" style protocol:
    #
    # For each query "? x y" the judge returns:
    #   '1' if (a ^ x) > (b ^ y)
    #   '-1' if (a ^ x) < (b ^ y)
    #   '0' if equal
    #
    # But the given code compares answers as strings and only checks '1'
    # explicitly, treating all other non-'1' as "else".
    #
    # The concrete protocol used in many solutions is:
    #   input is '1'  if (a ^ x) > (b ^ y)
    #   input is '-1' if (a ^ x) < (b ^ y)
    #   input is '0'  if equal
    #
    # The provided code matches that: ans00, ans11, ans01 are string results.
    #
    # We'll implement that oracle and then run the same logic, but without I/O.

    # Deterministic hidden a,b from n
    # Ensure they stay within 30 bits to match 2**29 bit-iteration
    a_hidden = (n * 1234567) & ((1 << 30) - 1)
    b_hidden = (n * 890123) & ((1 << 30) - 1)

    def oracle(x, y):
        va = a_hidden ^ x
        vb = b_hidden ^ y
        if va > vb:
            return '1'
        elif va < vb:
            return '-1'

        else:
            return '0'

    # Rewritten original logic
    ans00 = oracle(0, 0)
    xr = 0
    a = 0
    b = 0
    cb = 2 ** 29
    while cb:
        ans11 = oracle(xr + cb, cb)
        if ans11 == ans00:
            ans01 = oracle(xr, cb)
            if ans01 == '1':
                a += cb
                b += cb

        else:
            ans00 = oracle(xr, cb)
            if ans11 == '1':
                b += cb

            else:
                a += cb
            xr += cb
        cb //= 2

    # The original program prints the discovered a and b.
    # For complexity experiments we just print them once.
    # print(a, b)
    pass
if __name__ == "__main__":
    # Example: run with a chosen scale n
    main(10)