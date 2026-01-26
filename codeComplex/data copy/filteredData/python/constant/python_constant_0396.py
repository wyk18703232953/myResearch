def main(n):
    # Generate two deterministic binary strings of length n
    # Pattern: alternate '0' and '1' with different phases for two rows
    row1 = [('0' if i % 2 == 0 else '1') for i in range(n)]
    row2 = [('1' if i % 3 == 0 else '0') for i in range(n)]
    b = [row1, row2]

    ans = 0
    a = []
    for i in range(n):
        ai = 0
        if b[0][i] == '0':
            ai += 1
        if b[1][i] == '0':
            ai += 1
        a.append(ai)
    prv = 0
    for i in range(n):
        if a[i] == 0:
            prv = 0
        elif a[i] == 1:
            if prv == 2:
                ans += 1
                prv = 0

            else:
                prv = 1
        elif a[i] == 2:
            if prv == 2:
                ans += 1
                prv = 1
            elif prv == 1:
                ans += 1
                prv = 0

            else:
                prv = 2
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)