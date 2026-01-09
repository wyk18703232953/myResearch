def main(n):
    # Generate deterministic input of size n:
    # We create n tiles as strings like "1m", "2p", "3s" in a fixed cyclic pattern.
    # This emulates the original space-separated input line.
    suits = ['m', 'p', 's']
    tiles = []
    for i in range(n):
        num = (i % 9) + 1          # 1..9
        suit = suits[(i // 9) % 3] # cycle suits every 9
        tiles.append(f"{num}{suit}")
    s = " ".join(tiles)

    s = s.split(' ')

    M = [0] * 9
    P = [0] * 9
    S = [0] * 9

    for pile in s:
        if not pile:
            continue
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
            # print(0)
            pass
            return
        if P[i] == 3:
            # print(0)
            pass
            return
        if S[i] == 3:
            # print(0)
            pass
            return

    for i in range(7):
        if M[i] == 1 and M[i + 1] == 1 and M[i + 2] == 1:
            # print(0)
            pass
            return
        if P[i] == 1 and P[i + 1] == 1 and P[i + 2] == 1:
            # print(0)
            pass
            return
        if S[i] == 1 and S[i + 1] == 1 and S[i + 2] == 1:
            # print(0)
            pass
            return

    for i in range(9):
        if M[i] == 2:
            # print(1)
            pass
            return
        if P[i] == 2:
            # print(1)
            pass
            return
        if S[i] == 2:
            # print(1)
            pass
            return

    for i in range(8):
        if M[i] == 1 and M[i + 1] == 1:
            # print(1)
            pass
            return
        if P[i] == 1 and P[i + 1] == 1:
            # print(1)
            pass
            return
        if S[i] == 1 and S[i + 1] == 1:
            # print(1)
            pass
            return

    for i in range(7):
        if M[i] == 1 and M[i + 2] == 1:
            # print(1)
            pass
            return
        if P[i] == 1 and P[i + 2] == 1:
            # print(1)
            pass
            return
        if S[i] == 1 and S[i + 2] == 1:
            # print(1)
            pass
            return

    # print(2)
    pass
if __name__ == "__main__":
    main(14)