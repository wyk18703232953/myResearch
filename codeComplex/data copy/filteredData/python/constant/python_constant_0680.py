def main(n):
    # Deterministic construction of hidden numbers A and B based on n
    # to simulate the interactive judge for time complexity experiments.
    # Map n to two non-negative integers A and B in a deterministic way.
    A = 0
    B = 0
    for i in range(n):
        if i % 2 == 0:
            A |= (1 << (i % 30))
        if i % 3 == 0:
            B |= (1 << (i % 30))

    def query(c, d):
        # Simulated judge: compare (A xor c) and (B xor d)
        ac = A ^ c
        bd = B ^ d
        if ac > bd:
            return 1
        elif ac < bd:
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

    # Return the discovered pair and the hidden pair to keep everything deterministic
    return a, b, A, B


if __name__ == "__main__":
    # Example call for time complexity experiments
    result = main(1000)
    # print(result)
    pass