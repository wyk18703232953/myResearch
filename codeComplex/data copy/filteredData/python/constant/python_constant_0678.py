def main(n):
    # Interpret n as the target hidden difference sign pattern seed
    # For determinism, build hidden numbers A and B based solely on n
    # so that A - B has a predictable relation to n.
    # This replaces the interactive judge.
    max_bits = 30

    # Deterministically construct hidden numbers A and B from n
    # Example scheme: encode n in lower bits of A, and in a shifted way in B
    A = 0
    B = 0
    for i in range(max_bits):
        if (n >> i) & 1:
            A |= (1 << i)
        if (n >> ((i + 1) % max_bits)) & 1:
            B |= (1 << i)

    def judge(x, y):
        diff = (A - x) - (B - y)
        if diff > 0:
            return 1
        elif diff < 0:
            return -1

        else:
            return 0

    # Original logic starts here, with judge() replacing input/print interaction
    t = judge(0, 0)
    s = [0] * 31
    s[30] = 1 if t == 1 else -1

    a = 0
    b = 0
    for i in range(30, 0, -1):
        c = (1 << (i - 1)) + a
        d = b
        ans1 = judge(c, d)
        c = a
        d = (1 << (i - 1)) + b
        ans2 = judge(c, d)
        if ans1 == -1 and ans2 == 1:
            a += 1 << (i - 1)
            b += 1 << (i - 1)
            s[i - 1] = s[i]
        elif ans1 == 1 and ans2 == -1:
            # a and b unchanged
            s[i - 1] = s[i]

        else:
            s[i - 1] = ans1
            if s[i] == 1:
                a += 1 << (i - 1)
                # b unchanged

            else:
                # a unchanged
                b += 1 << (i - 1)

    # Final result (a, b) is returned for deterministic observation
    return a, b, A, B


if __name__ == "__main__":
    # Example deterministic call; change n to scale input complexity
    res = main(10)
    # print(res)
    pass