def main(n):
    # n: size parameter, mapped to number of rows
    # m: number of columns, tied to n for scalability
    if n <= 0:
        return
    m = n

    listi = []
    for i in range(n):
        # Deterministic construction of each row with exactly one 'B'
        # Columns are indexed 0..m-1; put 'B' at position i % m
        pos = i % m
        row = ''.join('B' if j == pos else '.' for j in range(m))
        listi.append(row)

    rownum = 0
    flag = False
    for row in listi:
        for letter in row:
            if "B" in row:
                p = row.index("B")
                s = row[::-1]
                q = abs(m - s.index("B") - 1)

                if p == q:
                    # print(rownum + 1, row.index(row[p]) + 1)
                    pass
                    flag = True
                    break
                mr = (q + p) / 2
                length = abs(q - p + 1)
                rn = rownum + length // 2
                # print(rn + 1, int(mr + 1))
                pass
                flag = True
                break
        if flag:
            break
        rownum += 1


if __name__ == "__main__":
    main(5)