def main(n):
    # n controls both dimensions of the grid: n x n
    # generate a deterministic grid with a single 'B' block pattern
    m = n
    li = [['W' for _ in range(m)] for _ in range(n)]

    # place a deterministic block of 'B's depending on n
    if n > 0:
        top = n // 4
        bottom = (3 * n) // 4
        left = n // 3
        right = (2 * n) // 3
        for i in range(top, bottom + 1):
            if 0 <= i < n:
                for j in range(left, right + 1):
                    if 0 <= j < m:
                        li[i][j] = 'B'

    for j in range(m):
        flag = False
        for i in range(n):
            if li[i][j] == "B":
                flag = True
                position1 = i
                break
        if flag == True:
            break

    for j in range(m - 1, -1, -1):
        flag = False
        for i in range(n - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position2 = i
                break
        if flag == True:
            break

    for i in range(n):
        flag = False
        for j in range(m):
            if li[i][j] == "B":
                flag = True
                position3 = j
                break
        if flag == True:
            break

    for i in range(n - 1, -1, -1):
        flag = False
        for j in range(m - 1, -1, -1):
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