def main(n):
    # Generate deterministic input list of length n
    # Mix even and odd numbers in a predictable pattern
    l = [(i * 2 if i % 3 == 0 else i * 2 + 1) for i in range(1, n + 1)]

    c1 = 0
    c2 = 0
    for i in l:
        if i % 2 == 0:
            c1 += 1

        else:
            c2 += 1

    lasteven = -1
    lastodd = -1

    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            lasteven = i
            break

    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 != 0:
            lastodd = i
            break

    if c1 == 1:
        # print(lasteven + 1)
        pass

    else:
        # print(lastodd + 1)
        pass
if __name__ == "__main__":
    main(10)