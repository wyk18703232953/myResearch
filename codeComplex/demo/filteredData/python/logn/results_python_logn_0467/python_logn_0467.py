def main(n):
    def qu(a, b):
        # Deterministic replacement for interactive query:
        # Original qu(a,b) returned -1, 0, or 1 based on hidden numbers.
        # Here we fix hidden A,B as functions of n for repeatability.
        A = n * 2 + 1
        B = n * 3 + 2
        if a ^ A < b ^ B:
            return -1
        elif a ^ A > b ^ B:
            return 1

        else:
            return 0

    a = 0
    b = 0
    big = qu(a, b)
    for i in range(29, -1, -1):
        x = 2 ** i
        f = qu(a + x, b)
        l = qu(a, b + x)
        if l == f:
            if big == 1:
                a += x

            else:
                b += x
            big = f
        elif f == -1:
            a += x
            b += x
    # For time-complexity experiments, just return the result instead of printing
    return a, b


if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size logically
    result = main(10)
    # print(result)
    pass