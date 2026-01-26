def main(n):
    # Interpret n as the number of time points
    # Also derive m deterministically from n
    if n <= 0:
        return

    # Deterministic choice for m as a function of n
    m = max(1, n // 2)

    b = []
    d = []

    for x in range(n):
        # Deterministically generate (a, c) for each x
        # a in range 0..23 (hours), c in range 0..59 (minutes)
        a = (x * 7 + n) % 24
        c = (x * 11 + n // 3) % 60

        if x == 0:
            if (a * 60) + c > m:
                b.append("0 0")
            d.append((a * 60) + c)

        else:
            if ((a * 60) + c) - d[-1] > (m * 2) + 1:
                f = d[-1] + m + 1
                b.append(str(f // 60) + " " + str(f % 60))
            d.append((a * 60) + c)

    if len(b) == 0:
        f = d[-1] + m + 1
        b.append(str(f // 60) + " " + str(f % 60))

    # For experiment purposes, keep the same behavior: print first element of b
    # print(b[0])
    pass
if __name__ == "__main__":
    # Example deterministic call; change n to scale input size
    main(10)