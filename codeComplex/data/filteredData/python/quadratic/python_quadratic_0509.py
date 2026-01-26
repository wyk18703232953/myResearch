def main(n):
    # Map n to grid dimensions: choose square-ish grid
    if n <= 0:
        return
    m = n

    # Deterministically generate a pattern of '#' and '.'
    # Example pattern: '#' if (i*j) % 7 < 3, else '.'
    arr = []
    for i in range(n):
        row_chars = []
        for j in range(m):
            if (i * j) % 7 < 3:
                row_chars.append('#')

            else:
                row_chars.append('.')
        arr.append(''.join(row_chars))

    arr1 = [[0] * m for _ in range(n)]

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
    # Example deterministic call for complexity experiments
    main(100)