def main(n):
    # Map n to matrix dimensions: n x n, with minimum size 3x3
    if n < 3:
        n = 3
    m = n

    # Deterministically generate the grid l (list of list of characters)
    # Pattern: '#' where (i + j) % 4 == 0, else '.'
    l = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 4 == 0:
                row.append("#")
            else:
                row.append(".")
        l.append(row)

    # Initialize ans matrix with '.'
    ans = []
    for i in range(n):
        ans.append([])
        for j in range(m):
            ans[-1].append(".")

    # Core algorithm logic preserved
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

    flag = True
    for i in range(n):
        for j in range(m):
            if l[i][j] != ans[i][j]:
                flag = False
                break
        if flag is False:
            break

    if flag is True:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # Example deterministic call; change the argument to test other scales
    main(10)