def main(n):
    # In the original interactive problem, a and b are unknown.
    # For deterministic testing, we generate a and b from n.
    # Let a and b be n-bit numbers derived deterministically.
    # For example:
    #   a = (n * 1234567) & ((1 << n) - 1)
    #   b = (n * 891011) & ((1 << n) - 1)
    # Limit n to [1, 60] for practical bit sizes.
    if n <= 0:
        n = 1
    if n > 60:
        n = 60

    global a, b
    a = (n * 1234567) & ((1 << n) - 1)
    b = (n * 891011) & ((1 << n) - 1)

    def get_ans(c, d, curaM, curbM):
        a_ = a ^ c ^ curaM
        b_ = b ^ d ^ curbM

        if a_ > b_:
            return 1
        if a_ < b_:
            return -1
        return 0

    curaM = 0
    curbM = 0
    curC = get_ans(0, 0, 0, 0)

    # The original code uses 30 bits (from 29 down to 0).
    # To scale with n, we use min(n, 30) bits.
    max_bit = min(n, 30)

    for i in range(max_bit - 1, -1, -1):
        ans1 = get_ans(1 << i, 0, curaM, curbM)
        ans2 = get_ans(0, 1 << i, curaM, curbM)

        if ans1 * ans2 >= 0:
            if curC == 1:
                curaM |= 1 << i
            elif curC == -1:
                curbM |= 1 << i
            curC = ans1

        else:
            if ans1 < 0:
                curaM |= 1 << i
                curbM |= 1 << i

    # For time-complexity experiments, we simply return the result.
    return curaM, curbM


if __name__ == "__main__":
    # Example deterministic call for n = 30
    res = main(30)
    # print(res)
    pass