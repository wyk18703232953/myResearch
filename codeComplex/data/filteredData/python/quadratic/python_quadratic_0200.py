def main(n):
    # Interpret n as both number of rows (s) and columns (l)
    s = n
    l = n

    if s == 0 or l == 0:
        # print('NO')
        pass
        return

    # Deterministic generation of sig: s rows, each a list of l digits (0-9)
    sig = []
    for i in range(s):
        row = [((i * 7 + j * 3) % 10) for j in range(l)]
        sig.append(row)

    utp = []
    for i in range(l):
        out = 0
        for x in range(s):
            out += sig[x][i]
        utp.append(out)

    sig = sorted(sig, key=sum)

    for i in range(s):
        res1 = 0
        for x in range(l):
            if utp[x] - sig[i][x] <= 0:
                break

            else:
                res1 += 1
        if res1 == l:
            # print('YES')
            pass
            return

    # print('NO')
    pass
if __name__ == "__main__":
    main(5)