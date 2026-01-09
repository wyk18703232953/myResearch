def ask(a, b, secret):
    return (a - secret) <= (b - secret)


def solve(M, secret):
    a, b = 0, 0
    less = ask(0, 0, secret)

    for i in range(M - 1, -1, -1):
        bit = 1 << i

        if less:
            if not ask(a | bit, b | bit, secret):
                b |= bit
                less = ask(a, b, secret)
            elif ask(a | bit, b, secret):
                a |= bit
                b |= bit

        else:
            if ask(a | bit, b | bit, secret):
                a |= bit
                less = ask(a, b, secret)
            elif ask(a | bit, b, secret):
                a |= bit
                b |= bit

    return a, b


def main(n):
    M = n
    secret = n * 7 + 3
    a, b = solve(M, secret)
    # print(a, b)
    pass
if __name__ == "__main__":
    main(30)