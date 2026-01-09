import math


mod = 10 ** 9 + 7


def main(n):
    # n controls the hidden pair (A, B) that the interactive algorithm tries to discover.
    # We deterministically generate A and B from n.
    # Keep them within 30 bits since the original algorithm loops i from 29 down to 0.
    A = (n * 1234567) & ((1 << 30) - 1)
    B = (n * 7654321 + 42) & ((1 << 30) - 1)

    def ask(x, y):
        # Simulate the judge's response:
        # return sign((A xor B) - (x xor y))
        val = (A ^ B) - (x ^ y)
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    a = b = 0
    cond = ask(a, b)
    for i in range(29, -1, -1):
        if cond:
            x = a + (1 << i)
            y = b + (1 << i)
            n_cond = ask(x, y)
            if cond == n_cond:
                if cond == 1:
                    n_cond1 = ask(x, b)

                else:
                    n_cond1 = ask(a, y)
                if cond != n_cond1:
                    a = x
                    b = y

            else:
                if cond == 1:
                    a = x

                else:
                    b = y
                cond = ask(a, b)

        else:
            x = a + (1 << i)
            y = b + (1 << i)
            n_cond = ask(x, b)
            if n_cond == -1:
                a = x
                b = y

    # For time-complexity experiments we return the discovered (a, b)
    # and the hidden (A, B) so a caller can verify correctness if desired.
    return a, b, A, B


if __name__ == "__main__":
    # Example deterministic call for timing/verification
    result = main(10)
    # print(result)
    pass