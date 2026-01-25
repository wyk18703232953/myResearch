import string

def main(n):
    # n: length of the strings s and t
    if n <= 0:
        print(0)
        print(-1, -1)
        return

    letters = string.ascii_lowercase

    # Deterministically generate s and t of length n
    # s[i] and t[i] are periodic over the lowercase alphabet
    s = ''.join(letters[i % 26] for i in range(n))
    t = ''.join(letters[(i * 2) % 26] for i in range(n))

    x, i, j = 0, -1, -1
    sc_dict = {c: set() for c in letters}
    tc_dict = {c: set() for c in letters}
    sti_dict, tsi_dict = dict(), dict()

    for ci, sc, tc in zip(range(n), s, t):
        if sc == tc:
            continue
        sc_dict[sc].add(tc)
        tc_dict[tc].add(sc)
        sti_dict[sc + tc] = ci
        tsi_dict[tc + sc] = ci
        x += 1

    for c in letters:
        cs = sc_dict[c] & tc_dict[c]
        if not cs:
            continue
        c2 = cs.pop()
        x -= 2
        i = sti_dict[c + c2] + 1
        j = tsi_dict[c + c2] + 1
        break
    else:
        for c in letters:
            if not sc_dict[c] or not tc_dict[c]:
                continue
            x -= 1
            i = sti_dict[c + sc_dict[c].pop()] + 1
            j = tsi_dict[c + tc_dict[c].pop()] + 1
            break

    print(x)
    print(i, j)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(1000)