def main(n):
    # Interpret n as both number of rows and columns of a binary matrix
    m = n

    # Deterministically generate n binary strings of length m
    # Pattern: t[i][j] = '1' if (i + j) % 3 == 0 else '0'
    s = [[] for _ in range(n)]
    l = [0] * m
    f = 0

    for i in range(n):
        t = ''.join('1' if (i + j) % 3 == 0 else '0' for j in range(m))
        for j in range(m):
            if t[j] == "1":
                l[j] += 1
                s[i].append(j)

    for i in range(n):
        r = set(l[c] - 1 for c in s[i])
        if 0 not in r:
            f = not f
            break
    # print("YNEOS"[not f::2])
    pass
if __name__ == "__main__":
    main(10)