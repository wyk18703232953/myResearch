def main(n):
    # Interpret n as grid size: n x n
    rows = n
    cols = n

    # Deterministic grid generation:
    # 'B' on and below the main diagonal, '.' elsewhere
    a = [['B' if j <= i else '.' for j in range(cols)] for i in range(rows)]

    temp = 0
    pos1 = 0
    pos2 = 0

    for i in range(rows):
        ok = False
        for j in range(cols):
            if a[i][j] == "B":
                pos1 = i
                pos2 = j
                temp += 1
                temp2 = j
                if j != cols - 1:
                    ok = True
                    while True:
                        ok2 = False
                        if temp2 == cols - 1:
                            ok2 = True
                            break
                        if a[i][temp2 + 1] != "B":
                            ok2 = True
                            break
                        temp += 1
                        temp2 += 1
                elif j == cols - 1:
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
    # Example call; adjust n as needed for experiments
    main(5)