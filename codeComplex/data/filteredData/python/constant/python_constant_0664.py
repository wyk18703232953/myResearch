import math


mod = 10 ** 9 + 7


def create_hidden_pair(n):
    # Deterministically create hidden a0, b0 from n
    # Bound them within 30 bits since original code loops 29..0
    a0 = (n * 1234567 + 89) & ((1 << 30) - 1)
    b0 = (n * 7654321 + 101) & ((1 << 30) - 1)
    return a0, b0


def compare(x, y, a0, b0):
    # Simulate interactive judge:
    # return 1 if (x ^ a0) > (y ^ b0)
    # return 0 if equal
    # return -1 if less
    vx = x ^ a0
    vy = y ^ b0
    if vx > vy:
        return 1
    elif vx < vy:
        return -1

    else:
        return 0


def main(n):
    a0, b0 = create_hidden_pair(n)

    def ask(x, y):
        return compare(x, y, a0, b0)

    a = 0
    b = 0
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

    # For determinism and to avoid I/O overhead in experiments, just return result
    return a, b, a0, b0


if __name__ == "__main__":
    # Example deterministic call for benchmarking
    res = main(10)
    # Print to observe behavior (can be removed in pure benchmarking)
    # print(res)
    pass