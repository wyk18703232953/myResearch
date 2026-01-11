def main(n):
    # Deterministically generate exactly 3 two-character strings similar to the original expectation
    # Map n to three "tiles": each tile is a suit (A,B,C,...) and a rank (1..9), all as strings
    # This keeps structure: e.g. ["1a","2a","3a"] etc., but here rank first, suit second, both as chars
    n = max(1, n)
    # Generate suits as letters cycling from 'a'
    suits = [chr(ord('a') + (i % 3)) for i in range(3)]
    # Generate ranks as digits 1..9 cycling based on n
    ranks = [str((n + i) % 9 + 1) for i in range(3)]
    a = [ranks[i] + suits[i] for i in range(3)]

    a.sort()
    if a[0] == a[1] == a[2]:
        # print(0)
        pass
        return
    elif a[0] == a[1] or a[1] == a[2]:
        # print(1)
        pass
        return

    a1 = []
    for i in range(3):
        a1.append([int(a[i][0]), a[i][1]])
    a1.sort()
    if a1[1][1] == a1[2][1] == a1[0][1]:
        if a1[0][0] == a1[1][0] - 1 and a1[0][0] == a1[2][0] - 2:
            # print(0)
            pass
            return
        for i in range(3):
            for j in range(3):
                if abs(a1[i][0] - a1[j][0]) == 1 or abs(a1[i][0] - a1[j][0]) == 2:
                    # print(1)
                    pass
                    return
        # print(2)
        pass
        return
    for i in range(3):
        for j in range(i + 1, 3):
            if a1[i][1] == a1[j][1]:
                if a1[i][0] == a1[j][0] - 1 or a1[i][0] == a1[j][0] - 2:
                    # print(1)
                    pass

                else:
                    # print(2)
                    pass
                return
    # print(2)
    pass
if __name__ == "__main__":
    main(10)