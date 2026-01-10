def main(n):
    # Generate deterministic input: three "tile" strings like "1a", "2b", ...
    # We'll cycle ranks 1-9 and suits 'a','b','c' based on n.
    ranks = [str((n + i) % 9 + 1) for i in range(3)]
    suits_list = ['a', 'b', 'c']
    suits = [suits_list[(n + i) % 3] for i in range(3)]
    s = [ranks[i] + suits[i] for i in range(3)]

    b = []
    b.append((s[0][1], int(s[0][0])))
    b.append((s[1][1], int(s[1][0])))
    b.append((s[2][1], int(s[2][0])))
    b.sort()
    if (b[0][0] == b[1][0] and b[1][0] == b[2][0]):
        if (b[0] == b[1] and b[1] == b[2]):
            print(0)
        elif (b[0][1] + 1 == b[1][1] and b[1][1] + 1 == b[2][1]):
            print(0)
        elif (b[0] == b[1]):
            print(1)
        elif (b[1] == b[2]):
            print(1)
        elif b[0][1] + 1 == b[1][1]:
            print(1)
        elif b[0][1] + 2 == b[1][1]:
            print(1)
        elif b[1][1] + 1 == b[2][1]:
            print(1)
        elif b[1][1] + 2 == b[2][1]:
            print(1)
        elif b[0][1] + 1 == b[2][1]:
            print(1)
        elif b[0][1] + 2 == b[2][1]:
            print(1)
        else:
            print(2)
    elif (b[0][0] != b[1][0] and b[1][0] != b[2][0] and b[2][0] != b[0][0]):
        print(2)
    elif b[0][0] == b[1][0]:
        if b[0] == b[1]:
            print(1)
        elif b[0][1] + 1 == b[1][1]:
            print(1)
        elif b[0][1] + 2 == b[1][1]:
            print(1)
        else:
            print(2)
    elif b[1][0] == b[2][0]:
        if (b[1] == b[2]):
            print(1)
        elif b[1][1] + 1 == b[2][1]:
            print(1)
        elif b[1][1] + 2 == b[2][1]:
            print(1)
        else:
            print(2)
    else:
        print(2)


if __name__ == "__main__":
    main(1)