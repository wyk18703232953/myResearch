def main(n):
    # Ensure n is non-negative
    if n < 0:
        n = 0

    # Deterministically generate s and t based on n
    # Use lowercase letters; pattern ensures both matches and mismatches as n grows
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    la = len(alphabet)

    # s[i] cycles forward through alphabet, t[i] is shifted by 1
    s = "".join(alphabet[i % la] for i in range(n))
    t = "".join(alphabet[(i + 1) % la] for i in range(n))

    value = {}
    li = []
    res1 = 0
    res2 = res3 = -1

    for i in range(n):
        if s[i] != t[i]:
            value[t[i]] = i
            res1 += 1
            li.append(i)

    p = sq = False
    for i in li:
        if s[i] in value:
            p = True
            res2 = i + 1
            f = value[s[i]]
            res3 = f + 1
            if s[f] == t[i]:
                sq = True
                break

    print(res1 - (2 if sq else 1 if p else 0))
    print(res2, res3)


if __name__ == "__main__":
    main(10)