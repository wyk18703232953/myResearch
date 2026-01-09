def main(n):
    # In the original interactive problem, the hidden values a0 and b0
    # are fixed but unknown to the program. Here we deterministically
    # generate them from n to remove any interaction.

    # Deterministic generation of hidden values based on n
    # Limit them into 30 bits since ops = 29 in original code
    a0 = (n * 1234567 + 890123) & ((1 << 30) - 1)
    b0 = (n * 7654321 + 210987) & ((1 << 30) - 1)

    # Simulate the judge's response for query "? c d"
    def judge(c, d):
        val1 = a0 ^ c
        val2 = b0 ^ d
        if val1 > val2:
            return 1
        elif val1 < val2:
            return -1

        else:
            return 0

    # Initial query equivalent to "? 0 0"
    agtb = judge(0, 0)

    a, b = 0, 0
    ops = 29
    for i in range(ops, -1, -1):
        c = a | (1 << i)
        d = b
        x = judge(c, d)

        c = a
        d = b | (1 << i)
        y = judge(c, d)

        if x != y:
            if y == 1:
                a = a | (1 << i)
                b = b | (1 << i)

        else:
            if agtb == 1:  # a > b
                a = a | (1 << i)

            else:
                b = b | (1 << i)
            agtb = x

    # Final output, plus also return values for programmatic use
    # print(a, b)
    pass
    return a, b, a0, b0


if __name__ == "__main__":
    # Example call for time-complexity experiments
    # You can vary n to scale the deterministically generated inputs
    main(10)