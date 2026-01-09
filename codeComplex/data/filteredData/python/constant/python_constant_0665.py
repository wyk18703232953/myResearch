def main(n):
    # In the original interactive problem, the judge holds hidden integers A and B,
    # and each query is of the form:
    #   print("?", x, y)
    #   e = sign((A ^ B) - (x ^ y))   or some related comparator
    # and finally outputs "!", A, B.
    #
    # For time-complexity experiments, we must remove interaction and instead
    # deterministically simulate the judge with some A, B derived from n.
    #
    # We choose deterministic A, B based on n and bit-length 30:
    #   A = n & ((1 << 30) - 1)
    #   B = (A ^ ((1 << 30) - 1))  (bitwise complement within 30 bits)
    # This is arbitrary but fixed and reproducible.
    #
    # We then implement the same protocol locally. From patterns in typical
    # problems, the judge's reply e corresponds to:
    #   e = sign((A ^ B) - (x ^ y))
    # where sign(z) is:
    #   1  if z > 0
    #   0  if z == 0
    #  -1  if z < 0
    #
    # This matches the usage of values {-1, 0, 1} in the code.

    def judge_query(x, y, A, B):
        z = (A ^ B) - (x ^ y)
        if z > 0:
            return 1
        elif z < 0:
            return -1

        else:
            return 0

    # Deterministically define hidden numbers A, B from n
    MASK = (1 << 30) - 1
    A = n & MASK
    B = A ^ MASK

    # Now run the original algorithm, but replace input()/print to the judge by local calls
    # and accumulate some operations to give the algorithm something to do.
    astr = "0" * 30
    bstr = "0" * 30

    # Initial query
    e = judge_query(0, 0, A, B)
    abig = e

    for i in range(30):
        if abig == 0:
            x = int(astr, 2) + (1 << (29 - i))
            y = int(bstr, 2)
            e = judge_query(x, y, A, B)
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
            x = int(astr, 2) + (1 << (29 - i))
            y = int(bstr, 2) + (1 << (29 - i))
            e = judge_query(x, y, A, B)
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
                x2 = int(astr, 2)
                y2 = int(bstr, 2)
                abig = judge_query(x2, y2, A, B)

            else:
                x3 = int(astr, 2) + (1 << (29 - i))
                y3 = int(bstr, 2)
                e = judge_query(x3, y3, A, B)
                if e == -1:
                    if i < 29:
                        astr = astr[:i] + "1" + astr[i + 1:]
                        bstr = bstr[:i] + "1" + bstr[i + 1:]

                    else:
                        astr = astr[:i] + "1"
                        bstr = bstr[:i] + "1"

    # Final computed numbers (the algorithm's reconstruction)
    a_ans = int(astr, 2)
    b_ans = int(bstr, 2)

    # To keep side effects similar to the original (for completeness),
    # we print the final result.
    # print(a_ans, b_ans)
    pass
    return a_ans, b_ans


if __name__ == "__main__":
    # Example deterministic call for benchmarking with some n
    main(123456789)