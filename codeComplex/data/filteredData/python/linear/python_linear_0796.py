def main(n):
    # Generate deterministic test data: n tiles in Mahjong-like notation.
    # Tile types cycle through 'm', 'p', 's'; numbers cycle 1..9.
    tiles = []
    suits = ['m', 'p', 's']
    for i in range(n):
        num = (i % 9) + 1
        suit = suits[i % 3]
        tiles.append(str(num) + suit)
    s = " ".join(tiles)

    parts = s.split(' ')

    M = [0] * 9
    P = [0] * 9
    S = [0] * 9

    for pile in parts:
        pile = list(pile)
        num = int(pile[0])
        tile = pile[1]

        if tile == 's':
            S[num - 1] += 1
        elif tile == 'p':
            P[num - 1] += 1
        elif tile == 'm':
            M[num - 1] += 1

    for i in range(9):
        if M[i] == 3:
            print(0)
            return
        if P[i] == 3:
            print(0)
            return
        if S[i] == 3:
            print(0)
            return

    for i in range(7):
        if M[i] == 1 and M[i + 1] == 1 and M[i + 2] == 1:
            print(0)
            return
        if P[i] == 1 and P[i + 1] == 1 and P[i + 2] == 1:
            print(0)
            return
        if S[i] == 1 and S[i + 1] == 1 and S[i + 2] == 1:
            print(0)
            return

    for i in range(9):
        if M[i] == 2:
            print(1)
            return
        if P[i] == 2:
            print(1)
            return
        if S[i] == 2:
            print(1)
            return

    for i in range(8):
        if M[i] == 1 and M[i + 1] == 1:
            print(1)
            return
        if P[i] == 1 and P[i + 1] == 1:
            print(1)
            return
        if S[i] == 1 and S[i + 1] == 1:
            print(1)
            return

    for i in range(7):
        if M[i] == 1 and M[i + 2] == 1:
            print(1)
            return
        if P[i] == 1 and P[i + 2] == 1:
            print(1)
            return
        if S[i] == 1 and S[i + 2] == 1:
            print(1)
            return

    print(2)


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(14)