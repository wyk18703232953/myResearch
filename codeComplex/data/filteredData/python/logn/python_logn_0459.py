def main(n):
    # In the original interactive problem, there is a hidden pair (A, B)
    # and queries of the form: given x, y, return sign((A^x) - (B^y)).
    # For determinism and scalability, we generate a hidden (A, B) from n.
    # Let A and B be non-negative integers with at most 30 bits.
    # We construct A and B deterministically from n.
    A = n & ((1 << 30) - 1)
    B = ((n * 3 + 7) ^ (n << 1)) & ((1 << 30) - 1)

    def judge(x, y):
        ax = A ^ x
        by = B ^ y
        if ax < by:
            return -1
        elif ax == by:
            return 0

        else:
            return 1

    # Original algorithm logic, replacing interactive I/O with judge calls.
    e = judge(0, 0)
    astr = "000000000000000000000000000000"
    bstr = "000000000000000000000000000000"
    abig = e
    for i in range(30):
        if abig == 0:
            e = judge(int(astr, 2) + 2 ** (29 - i), int(bstr, 2))
            if e == 1:
                continue

            else:
                if i < 29:
                    astr = astr[:i] + "1" + astr[i + 1:]
                    bstr = bstr[:i] + "1" + bstr[i + 1:]

                else:
                    astr = astr[:i] + "1"
                    bstr = bstr[:i] + "1"

        else:
            e = judge(int(astr, 2) + 2 ** (29 - i), int(bstr, 2) + 2 ** (29 - i))
            if e == -abig:
                if abig == 1:
                    if i < 29:
                        astr = astr[:i] + "1" + astr[i + 1:]

                    else:
                        astr = astr[:i] + "1"

                else:
                    if i < 29:
                        bstr = bstr[:i] + "1" + bstr[i + 1:]

                    else:
                        bstr = bstr[:i] + "1"
                abig = judge(int(astr, 2), int(bstr, 2))

            else:
                e = judge(int(astr, 2) + 2 ** (29 - i), int(bstr, 2))
                if e == -1:
                    if i < 29:
                        astr = astr[:i] + "1" + astr[i + 1:]
                        bstr = bstr[:i] + "1" + bstr[i + 1:]

                    else:
                        astr = astr[:i] + "1"
                        bstr = bstr[:i] + "1"
    a_res = int(astr, 2)
    b_res = int(bstr, 2)
    # For experiment purposes, return results instead of printing with protocol markers
    return a_res, b_res, A, B


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    result = main(10)
    # print(result)
    pass