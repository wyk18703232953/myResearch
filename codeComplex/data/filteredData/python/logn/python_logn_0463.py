def main(n):
    # For this interactive-origin problem, the underlying logic is:
    # there exist hidden integers a0, b0, and every query "? x y"
    # returns sign(a0 ^ x - (b0 ^ y)) ∈ {-1, 0, 1}.
    # The original code reconstructs a0, b0 using up to 30 bits.
    #
    # Here we remove all input/interactive aspects and instead:
    # - deterministically construct hidden a0, b0 from n,
    # - implement a deterministic "oracle" query function,
    # - run the original reconstruction algorithm using that oracle,
    # - return the reconstructed a, b to allow time complexity experiments.
    #
    # We keep 30 bits as in the original.
    MAX_BITS = 30

    # Deterministically generate hidden numbers a0, b0 from n
    # Ensure they are within 0..(2^MAX_BITS - 1)
    mask = (1 << MAX_BITS) - 1
    a0 = (n * 123456789 + 987654321) & mask
    b0 = (n * 987654321 + 123456789) & mask

    # Oracle: given x, y, return sign( (a0 ^ x) - (b0 ^ y) )
    def oracle(x, y):
        va = a0 ^ x
        vb = b0 ^ y
        if va > vb:
            return 1
        elif va < vb:
            return -1

        else:
            return 0

    # Begin reconstruction logic (adapted from original interactive code)

    # Initial query with (0, 0)
    t = oracle(0, 0)

    A = [-1] * MAX_BITS
    B = [-1] * MAX_BITS
    a = 0
    b = 0

    i = MAX_BITS - 1
    d = 1 << i
    while i >= 0:
        a += d
        b += d
        s = oracle(a, b)
        if s == -t:
            if s == 1:
                # According to original logic (though this branch is unreachable
                # when t = oracle(0, 0) ∈ {-1, 0, 1})
                A[i] = 0
                B[i] = 1
                b -= d
                t = oracle(a, b)
            elif s == -1:
                A[i] = 1
                a -= d
                B[i] = 0
                t = oracle(a, b)
        i -= 1
        d //= 2 if d > 0 else 0

    d = 1
    for j in range(MAX_BITS):
        if A[j] == -1:
            a ^= d
            s = oracle(a, b)
            if s == 1:
                A[j] = 1
                B[j] = 1

            else:
                A[j] = 0
                B[j] = 0
            a ^= d
        d <<= 1

    d = 1
    a = 0
    b = 0
    for i in range(MAX_BITS):
        a += d * A[i]
        b += d * B[i]
        d <<= 1

    # For experimentation, we return (reconstructed_a, reconstructed_b, true_a0, true_b0)
    return a, b, a0, b0


if __name__ == "__main__":
    # Example deterministic call for experimentation
    # You can change the argument here to scale the "input size"
    result = main(1000)
    # print(result)
    pass