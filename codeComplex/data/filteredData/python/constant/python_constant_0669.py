def main(n):
    # In the original interactive problem, an unknown comparator provides:
    #   t = sign(a_real - b_real)
    # for every query "? a b". The algorithm reconstructs a_real and b_real.
    #
    # For deterministic, scalable experiments, we:
    # - Fix a bit-width W (original code uses 30).
    # - Let n control the size by taking the lowest W bits of n as a_real,
    #   and the next W bits as b_real.
    # - Implement a local oracle query(a, b) that returns sign((a_real - a) - (b_real - b))
    #   exactly matching how the original t is used: each query returns sign(a_real - b_real)
    #   after applying current a, b.
    #
    # To stay faithful to the original logic, we reconstruct bits of a_real, b_real.

    W = 30  # bit width, consistent with original loops

    # Derive fixed "hidden" numbers from n, deterministically.
    mask = (1 << W) - 1
    a_real = n & mask
    b_real = (n >> W) & mask

    def sign(x):
        if x > 0:
            return 1
        if x < 0:
            return -1
        return 0

    def query(a, b):
        # What original t represents for each query:
        # t = sign((a_real ^ a) - (b_real ^ b)) is not correct for the original logic.
        # The original AtCoder solution for this problem (ABC187 F-like) actually
        # assumes oracle returns sign((a_real - a) - (b_real - b)) with a,b as candidates.
        return sign((a_real - a) - (b_real - b))

    # Begin port of the original algorithm, but using query() instead of input.

    # Initial query with a = 0, b = 0
    t = query(0, 0)

    A = [-1] * W
    B = [-1] * W
    a = 0
    b = 0

    i = W - 1
    d = 1 << i

    while i >= 0:
        a += d
        b += d
        s = query(a, b)
        if s != t:
            if s == 1:
                A[i] = 0
                B[i] = 1
                b -= d
                t = query(a, b)
            else:  # s == -1
                A[i] = 1
                a -= d
                B[i] = 0
                t = query(a, b)
        i -= 1
        d >>= 1

    d = 1
    for j in range(W):
        if A[j] == -1:
            a ^= d
            s = query(a, b)
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
    for i in range(W):
        a += d * A[i]
        b += d * B[i]
        d <<= 1

    # For experiment purposes, we return the reconstructed a, b and the ground truth a_real, b_real.
    # This allows checking correctness while avoiding any interactive IO.
    return a, b, a_real, b_real


if __name__ == "__main__":
    # Example deterministic call; change n to scale and vary inputs.
    result = main(123456789)
    # print(result)
    pass