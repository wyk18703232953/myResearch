def main(n):
    # Interpret n as grid size: n x n grid
    # Deterministically generate an n x n grid of '.' and '#'
    # Example pattern: '#' where (i + j) % 3 == 0, else '.'
    m = n
    arr = []
    arr1 = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 3 == 0:
                row.append('#')

            else:
                row.append('.')
        arr.append(''.join(row))
        arr1.append([0] * m)

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#' and i < n - 2 and j < m - 2:
                if (
                    arr[i][j + 1] == '#'
                    and arr[i][j + 2] == '#'
                    and arr[i + 1][j] == '#'
                    and arr[i + 2][j] == '#'
                    and arr[i + 2][j + 1] == '#'
                    and arr[i + 2][j + 2] == '#'
                    and arr[i + 1][j + 2] == '#'
                ):
                    arr1[i][j] = 1
                    arr1[i + 1][j] = 1
                    arr1[i + 2][j] = 1
                    arr1[i + 2][j + 1] = 1
                    arr1[i + 2][j + 2] = 1
                    arr1[i + 1][j + 2] = 1
                    arr1[i][j + 1] = 1
                    arr1[i][j + 2] = 1

    flag = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "#" and arr1[i][j] == 0:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(1000)