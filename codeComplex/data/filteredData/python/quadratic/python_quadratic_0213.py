from operator import *


def main(n):
    # Interpret n as the number of bitmasks; bit-length is derived deterministically
    if n <= 0:
        return "YES"

    bit_len = max(1, (n % 20) + 1)  # deterministic bit length between 1 and 20

    # Generate n deterministic integers that emulate binary input lines
    # x_i = ((i + 1) * (i + 2)) modulo (1 << bit_len)
    a = [(((i + 1) * (i + 2)) & ((1 << bit_len) - 1)) for i in range(n)]

    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x
    result = ("YES", "NO")[all(x & s & ~t for x in a)]
    return result


if __name__ == "__main__":
    # example call; change n to adjust input scale
    # print(main(10))
    pass