def main(n):
    import sys

    # Deterministic data generation based on n
    # We emulate an "oracle" that given queries (?, x, y) returns:
    #   0 if x == y
    #   1 if x < y
    #   2 if x > y
    # This matches the typical interactive problem style and keeps logic intact.
    #
    # Original code tries to deduce two unknown numbers A and B in [0, 2^30),
    # using queries on (hat1^bb, hat2) etc. Here we create deterministic A, B.
    #
    # Map n to A, B deterministically:
    #   A = n mod 2^30
    #   B = (3*n + 7) mod 2^30
    # These are fixed for given n.
    MOD = 1 << 30
    A = n % MOD
    B = (3 * n + 7) % MOD

    def oracle(x, y):
        # Return 0 if (A^x) == (B^y)
        #        1 if (A^x) <  (B^y)
        #        2 if (A^x) >  (B^y)
        v1 = A ^ x
        v2 = B ^ y
        if v1 == v2:
            return 0
        return 1 if v1 < v2 else 2

    bb = 0  # In interactive version this was random; here keep deterministic.

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
                    hat1 += 1 << i

                else:
                    hat2 += 1 << i
                lastresult = None
                continue
        lastresult = t1
        t3 = oracle(g1 ^ bb, hat2)
        if t3 == 1:
            pass

        else:
            hat1 += 1 << i
            hat2 += 1 << i

    # The original output: print('!', hat1^bb% (2**30), hat2)
    # Keep same structure without interactive markers.
    x_res = (hat1 ^ bb) % MOD
    y_res = hat2
    # print(x_res, y_res)
    pass
if __name__ == "__main__":
    # Example deterministic call; change n to scale input size / complexity.
    main(10)