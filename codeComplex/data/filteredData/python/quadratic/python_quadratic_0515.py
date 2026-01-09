def main(n):
    # Interpret n as both number of rows and columns for a square grid
    # Ensure minimum size of 3x3 to allow 3x3 pattern checks
    if n < 3:
        n = 3
    m = n

    # Deterministically generate the grid l (list of list of chars)
    # Pattern: form 3x3 blocks of '#' starting at positions where both indices are multiples of 4
    l = []
    for i in range(n):
        row = []
        for j in range(m):
            # Define top-left corners of 3x3 blocks
            if i + 2 < n and j + 2 < m and i % 4 == 0 and j % 4 == 0:
                # Inside a 3x3 block of '#'
                row.append('#')

            else:
                row.append('.')
        l.append(row)

    # Initialize ans grid with '.'
    ans = []
    for i in range(n):
        ans.append([])
        for j in range(m):
            ans[-1].append(".")

    # Core algorithm: detect 3x3 patterns of '#' around positions and mark them in ans
    for i in range(n - 2):
        for j in range(m - 2):
            if l[i][j] == "#":
                if (
                    l[i][j] == l[i][j + 1]
                    and l[i][j] == l[i][j + 2]
                    and l[i][j] == l[i + 1][j]
                    and l[i][j] == l[i + 1][j + 2]
                    and l[i][j] == l[i + 2][j]
                    and l[i][j] == l[i + 2][j + 1]
                    and l[i][j] == l[i + 2][j + 2]
                ):
                    ans[i][j] = "#"
                    ans[i][j + 1] = "#"
                    ans[i][j + 2] = "#"
                    ans[i + 1][j] = "#"
                    ans[i + 1][j + 2] = "#"
                    ans[i + 2][j] = "#"
                    ans[i + 2][j + 1] = "#"
                    ans[i + 2][j + 2] = "#"

    # Compare original grid with ans
    flag = True
    for i in range(n):
        for j in range(m):
            if l[i][j] != ans[i][j]:
                flag = False
                break
        if flag is False:
            break

    if flag is True:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)