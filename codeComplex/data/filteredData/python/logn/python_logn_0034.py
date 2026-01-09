def main(n):
    # Interpret n as the bit-length of l and r
    # Deterministically generate l and r such that 0 <= l <= r < 2^n
    # Example pattern:
    # l = number with alternating bits starting from 0: 0101...
    # r = number with alternating bits starting from 1: 1010...
    if n <= 0:
        l = 0
        r = 0

    else:
        l = 0
        r = 0
        for i in range(n):
            if i % 2 == 1:
                l |= (1 << i)

            else:
                r |= (1 << i)

    if l == r:
        # print(0)
        pass
        return

    l_bin = bin(l)[2:].zfill(64)
    r_bin = bin(r)[2:].zfill(64)
    i = 0
    while i < len(r_bin):
        if l_bin[i] == r_bin[i]:
            i += 1

        else:
            break
    rslt = len(r_bin[:i]) * '0' + len(r_bin[i:]) * '1'
    # print(int(rslt, 2))
    pass
if __name__ == "__main__":
    main(10)