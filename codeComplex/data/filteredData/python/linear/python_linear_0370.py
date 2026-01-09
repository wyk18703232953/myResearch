def main(n):
    # Map n to problem parameters
    m = n  # length of a
    # Deterministic generation of c and a
    c = [(i * 2) % (2 * n + 1) for i in range(n)]
    a = [(i * 3 + 1) % (2 * n + 1) for i in range(m)]

    x = 0
    for i in range(n):
        try:
            if a[0] >= c[i]:
                x += 1
                a.pop(0)
        except IndexError:
            pass

    # print(x)
    pass
if __name__ == "__main__":
    main(10)