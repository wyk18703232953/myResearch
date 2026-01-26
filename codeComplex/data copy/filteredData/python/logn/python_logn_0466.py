def solve(M, secret_a, secret_b):
    def ask(a, b):
        return (secret_a ^ a) - (secret_b ^ b) <= 0

    a, b = 0, 0
    less = ask(0, 0)

    for i in range(M - 1, -1, -1):
        bit = 1 << i

        if less:
            if not ask(a | bit, b | bit):
                b |= bit
                less = ask(a, b)
            elif ask(a | bit, b):
                a |= bit
                b |= bit

        else:
            if ask(a | bit, b | bit):
                a |= bit
                less = ask(a, b)
            elif ask(a | bit, b):
                a |= bit
                b |= bit

    return a, b


def main(n):
    M = n
    secret_a = sum(i * 3 for i in range(n)) & ((1 << M) - 1)
    secret_b = sum(i * 5 for i in range(n)) & ((1 << M) - 1)
    a, b = solve(M, secret_a, secret_b)
    # print(a, b)
    pass
if __name__ == "__main__":
    main(30)