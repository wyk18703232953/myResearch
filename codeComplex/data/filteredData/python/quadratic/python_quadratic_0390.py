def main(n):
    # Map n to matrix size: use n x n grid
    rows = n
    cols = n

    # Deterministically generate grid with some 'B' cells
    # Pattern: put 'B' on cells where (i + j) % k == 0 for a fixed k
    k = 3 if n >= 3 else 1
    li = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i + j) % k == 0:
                row.append('B')

            else:
                row.append('W')
        li.append(row)

    # Replicate original logic
    n_local = rows
    m_local = cols

    for j in range(m_local):
        flag = False
        for i in range(n_local):
            if li[i][j] == "B":
                flag = True
                position1 = i
                break
        if flag == True:
            break
    for j in range(m_local - 1, -1, -1):
        flag = False
        for i in range(n_local - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position2 = i
                break
        if flag == True:
            break
    for i in range(n_local):
        flag = False
        for j in range(m_local):
            if li[i][j] == "B":
                flag = True
                position3 = j
                break
        if flag == True:
            break
    for i in range(n_local - 1, -1, -1):
        flag = False
        for j in range(m_local - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position4 = j
                break
        if flag == True:
            break

    avg1 = (position1 + position2) // 2 + 1
    avg2 = (position3 + position4) // 2 + 1
    # print(avg1, avg2)
    pass
if __name__ == "__main__":
    main(10)