def main(n):
    # Generate deterministic input of two integers based on n
    # Map n to two numbers: a and b
    # For example: a = n, b = 2*n + 1
    r0 = n
    r1 = 2 * n + 1

    from operator import xor

    ms = xor(r0, r1)

    max_val = 0
    s = 1

    while ms > 0:
        ms >>= 1
        max_val += s
        s <<= 1

    # print(max_val)
    pass
if __name__ == "__main__":
    main(10)