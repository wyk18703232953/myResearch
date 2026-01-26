def main(n):
    # Interpret n as both s (rows) and l (columns) to scale input size as n^2
    s = n
    l = n

    # Handle the early-exit condition from original code
    if s == 0 or l == 0:
        # print("NO")
        pass
        return

    # Deterministically generate s rows, each a list of l digits (0 or 1)
    # using a simple arithmetic pattern
    sig = []
    for i in range(s):
        row = []
        for j in range(l):
            # Example deterministic pattern: (i + j) % 2
            row.append((i + j) % 2)
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
            # print("YES")
            pass
            return

    # print("NO")
    pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(5)