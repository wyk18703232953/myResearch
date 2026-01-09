def main(n):
    import sys

    # We interpret n as the upper bound (exclusive) for unknown integer A,B in [0, n)
    # To keep it within 30 bits as original code, cap at 2**30
    MAXV = 2 ** 30
    if n <= 0:
        n = 1
    if n > MAXV:
        n = MAXV

    # Deterministically construct "hidden" A,B from n
    # Ensure 0 <= A,B < n
    A = n // 2
    B = (n * 3) // 5
    A %= n
    B %= n

    # The interactive program logic works with a secret bb and queries of form f(x,y)
    # where responses depend on comparison between A^x and B^y.
    # From the code and typical pattern, we reconstruct the oracle:
    # Query: print('?', x, y); input t
    # t is:
    #   0 if A^x == B^y
    #   1 if A^x >  B^y
    #  -1 if A^x <  B^y
    #
    # Here we simulate this oracle directly.

    def oracle(x, y):
        ax = A ^ x
        by = B ^ y
        if ax == by:
            return 0
        elif ax > by:
            return 1

        else:
            return -1

    bb = 0  # in original, random; for determinism choose 0

    hat1 = 0
    hat2 = 0
    lastresult = None

    for i in range(29, -1, -1):
        g1 = hat1 + (1 << i)
        g2 = hat2 + (1 << i)

        if lastresult is None:
            t1 = oracle(hat1 ^ bb, hat2)

        else:
            t1 = lastresult

        if t1 != 0:
            t2 = oracle(g1 ^ bb, g2)
            if t1 != t2:
                if t1 == 1:
                    hat1 += (1 << i)

                else:
                    hat2 += (1 << i)
                lastresult = None
                continue

        lastresult = t1
        t3 = oracle(g1 ^ bb, hat2)
        if t3 == 1:
            pass

        else:
            hat1 += (1 << i)
            hat2 += (1 << i)

    result1 = (hat1 ^ bb) % (2 ** 30)
    result2 = hat2

    # For determinism and to make sure the function does real work, print results
    # (this is analogous to the original final output: print('!', ...)
    # print(result1, result2)
    pass
    return result1, result2


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10**5)