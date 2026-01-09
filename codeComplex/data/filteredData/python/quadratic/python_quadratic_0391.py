def main(n):
    # Interpret n as both number of rows and columns
    if n <= 0:
        return
    rows = n
    cols = n

    # Deterministically construct a grid with a block of 'B's
    # The block size and position depend on n but are fully deterministic.
    # Ensure at least one 'B'.
    block_height = max(1, n // 3)
    block_width = max(1, n // 4)

    top = n // 4
    left = n // 3
    if top + block_height > n:
        top = max(0, n - block_height)
    if left + block_width > n:
        left = max(0, n - block_width)

    li = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if top <= i < top + block_height and left <= j < left + block_width:
                row.append('B')

            else:
                row.append('.')
        li.append(row)

    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0

    for j in range(cols):
        flag = False
        for i in range(rows):
            if li[i][j] == "B":
                flag = True
                position1 = i
                break
        if flag:
            break

    for j in range(cols - 1, -1, -1):
        flag = False
        for i in range(rows - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position2 = i
                break
        if flag:
            break

    for i in range(rows):
        flag = False
        for j in range(cols):
            if li[i][j] == "B":
                flag = True
                position3 = j
                break
        if flag:
            break

    for i in range(rows - 1, -1, -1):
        flag = False
        for j in range(cols - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position4 = j
                break
        if flag:
            break

    avg1 = (position1 + position2) // 2 + 1
    avg2 = (position3 + position4) // 2 + 1
    # print(avg1, avg2)
    pass
if __name__ == "__main__":
    main(10)