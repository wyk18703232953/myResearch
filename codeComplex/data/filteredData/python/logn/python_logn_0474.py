def main(n):
    # In the original interactive problem, query(c, d) compares two hidden numbers A and B:
    #   returns 1  if (A ^ c) > (B ^ d)
    #   returns -1 if (A ^ c) < (B ^ d)
    #   returns 0  if equal
    # Here we deterministically generate such A, B from n.
    # Use 30-bit numbers to match the original loop range (0..29).
    A = (n * 1234567) & ((1 << 30) - 1)
    B = (n * 7654321 + 2024) & ((1 << 30) - 1)

    def query(c, d):
        x = A ^ c
        y = B ^ d
        if x > y:
            return 1
        elif x < y:
            return -1

        else:
            return 0

    a = 0
    b = 0
    big = query(0, 0)

    for i in range(29, -1, -1):
        p = query(a ^ (1 << i), b)
        q = query(a, b ^ (1 << i))
        if p == q:
            if big == 1:
                a ^= 1 << i

            else:
                b ^= 1 << i
            big = p
        elif p == -1:
            a ^= 1 << i
            b ^= 1 << i

    # For timing experiments, the print itself is not necessary for logic,
    # but we keep a simple deterministic output.
    # print(a, b)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for scaling experiments.
    main(10)