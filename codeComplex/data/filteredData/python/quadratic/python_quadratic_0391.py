def main(n):
    # Interpret n as the size of a square grid: n x n
    # Construct a deterministic grid of '.' with a solid 'B' block in the center.
    # This preserves the original logic which finds the center of the rectangle of 'B's.
    if n <= 0:
        return

    rows = n
    cols = n

    # Define a deterministic black square roughly centered in the grid.
    # For scalability, let its side length be max(1, n // 3).
    block_size = max(1, n // 3)
    top = (rows - block_size) // 2
    left = (cols - block_size) // 2
    bottom = top + block_size - 1
    right = left + block_size - 1

    li = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if top <= i <= bottom and left <= j <= right:
                row.append("B")

            else:
                row.append(".")
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
    # Example deterministic call; adjust n as needed for experiments
    main(9)