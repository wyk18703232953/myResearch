def main(n):
    # In the original interactive problem, m was fixed to 30.
    # Here we let m = n to scale the input size.
    m = n
    a, b = 0, 0
    fle = 1

    # Deterministic "hidden" values for simulation of interactive responses
    # These depend only on n, so they are deterministic and scalable.
    A = n * n + 1
    B = n * n + 2

    def cmp(x, y):
        if x < y:
            return -1
        elif x > y:
            return 1

        else:
            return 0

    for i in range(m):
        if fle:
            resp1 = cmp(a ^ A, b ^ B)
            fle = 0

        resp2 = cmp((a + 2 ** (m - 1 - i)) ^ A, (b + 2 ** (m - 1 - i)) ^ B)

        if resp1 == -1 and resp2 == 1:
            b += 2 ** (m - 1 - i)
            fle = 1
        elif resp1 == 1 and resp2 == -1:
            a += 2 ** (m - 1 - i)
            fle = 1

        else:
            fle = 0
            resp3 = cmp((a + 2 ** (m - 1 - i)) ^ A, b ^ B)
            if resp3 == -1:
                b += 2 ** (m - 1 - i)
                a += 2 ** (m - 1 - i)

    # Final result (simulating the original '! a b' output)
    # print(a, b)
    pass
if __name__ == "__main__":
    # Example: run with n = 30 to mimic original m=30
    main(30)