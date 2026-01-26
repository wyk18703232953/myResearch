def main(n):
    # Define matrix size based on n
    if n <= 0:
        return
    m = n

    # Deterministic generation of an n x m matrix of characters
    # Fill with 'A' and place a horizontal segment of 'B's on row r, from c_start to c_end
    # r, c_start, length are deterministic functions of n
    r = (n // 3) % n
    if m == 1:
        c_start = 0
        length = 1

    else:
        c_start = (n // 2) % (m - 1)
        length = min(max(1, n % m), m - c_start)
    c_end = c_start + length - 1

    a = []
    for i in range(n):
        row = []
        for j in range(m):
            if i == r and c_start <= j <= c_end:
                row.append("B")

            else:
                row.append("A")
        a.append(row)

    temp = 0
    pos1 = 0
    pos2 = 0
    for i in range(n):
        ok = False
        for j in range(m):
            if a[i][j] == "B":
                pos1 = i
                pos2 = j
                temp += 1
                temp2 = j
                ok2 = False
                if j != m - 1:
                    ok = True
                    while True:
                        if temp2 == m - 1:
                            ok2 = True
                            break
                        if a[i][temp2 + 1] != "B":
                            ok2 = True
                            break
                        temp += 1
                        temp2 += 1
                elif j == m - 1:
                    temp = 1
                    ok = True
                    break
                if ok2:
                    break
        if ok:
            break

    # print(temp // 2 + pos1 + 1, temp // 2 + pos2 + 1)
    pass
if __name__ == "__main__":
    main(10)