def main(n):
    # Deterministic generation of six side lengths based on n
    # Ensure they are positive and vary with n but stay small enough for printing
    base = max(1, n)
    a1 = base
    a2 = base + 1
    b1 = base % 5 + 1
    b2 = base % 7 + 2
    c1 = base % 6 + 1
    c2 = base % 4 + 3

    # Core logic from original program
    l = max([a1, a2, b1, b2, c1, c2])

    if (a1 * a2 + b1 * b2 + c1 * c2 != l ** 2):
        print(-1)
    else:
        if a1 > a2:
            a1, a2 = a2, a1
        if b1 > b2:
            b1, b2 = b2, b1
        if c1 > c2:
            c1, c2 = c2, c1

        if a2 == b2 and b2 == c2:
            print(l)
            for _ in range(a1):
                print('A' * a2)
            for _ in range(b1):
                print('B' * b2)
            for _ in range(c1):
                print('C' * c2)
        else:
            ls = [[a1, a2, 'A'], [b1, b2, 'B'], [c1, c2, 'C']]

            if b2 == l:
                ls[0], ls[1] = ls[1], ls[0]
            if c2 == l:
                ls[0], ls[2] = ls[2], ls[0]

            valid = True
            if ls[1][0] == ls[2][0]:
                pass
            elif ls[1][1] == ls[2][1]:
                ls[1][0], ls[1][1] = ls[1][1], ls[1][0]
                ls[2][0], ls[2][1] = ls[2][1], ls[2][0]
            elif ls[1][0] == ls[2][1]:
                ls[2][0], ls[2][1] = ls[2][1], ls[2][0]
            elif ls[1][1] == ls[2][0]:
                ls[1][0], ls[1][1] = ls[1][1], ls[1][0]
            else:
                valid = False

            if (ls[1][0] + ls[0][0] != l) or (ls[1][1] + ls[2][1] != l):
                valid = False

            if not valid:
                print(-1)
            else:
                print(l)
                for _ in range(ls[0][0]):
                    print(ls[0][2] * l)
                for _ in range(ls[1][0]):
                    print(ls[1][2] * ls[1][1] + ls[2][2] * ls[2][1])


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)