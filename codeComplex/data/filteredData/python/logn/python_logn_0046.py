def main(n):
    # Deterministically generate a and b based on n
    # Ensure a and b are positive and vary with n
    a = n
    b = 2 * n + 1

    b1 = bin(b)[2:]
    a1 = bin(a)[2:]
    if len(a1) == len(b1):
        d = (b ^ a)
        v = d.bit_length()
        result = int("0" + "1" * v, 2)

    else:
        result = int("1" * len(b1), 2)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)