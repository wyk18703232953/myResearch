def naiveSolve():
    return


def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))


def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))


def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))


def makeArr(defaultValFactory, dimensionArr):
    dv = defaultValFactory
    da = dimensionArr
    if len(da) == 1:
        return [dv() for _ in range(da[0])]
    else:
        return [makeArr(dv, da[1:]) for _ in range(da[0])]


inf = float('inf')
MOD = 10 ** 9 + 7


def solve_single_case(n, m, grid):
    columns = []
    for col in range(m):
        temp = [grid[i][col] for i in range(n)]
        columns.append(temp)

    valCol = []
    for i in range(n):
        for j in range(m):
            valCol.append((grid[i][j], j))
    valCol.sort(reverse=True)

    topCols = set()
    for val, col in valCol:
        topCols.add(col)
        if len(topCols) == n:
            break

    m2 = len(topCols)
    grid2 = [[-1 for _ in range(m2)] for _ in range(n)]
    topColsList = list(topCols)
    for j in range(m2):
        col = topColsList[j]
        for i in range(n):
            grid2[i][j] = grid[i][col]
    ans = -inf
    total_masks = n ** m2
    for mask_value in range(total_masks):
        mask = mask_value
        grid3 = [[-1 for _ in range(m2)] for _ in range(n)]
        for col in range(m2):
            shift = mask % n
            for row in range(n):
                grid3[row][col] = grid2[(shift + row) % n][col]
            mask //= n
        tempAns = 0
        for row in range(n):
            maxx = -inf
            for col in range(m2):
                if grid3[row][col] > maxx:
                    maxx = grid3[row][col]
            tempAns += maxx
        if tempAns > ans:
            ans = tempAns
    return ans


def main(n):
    # n controls the problem size:
    # use roughly sqrt(n) x sqrt(n) grids and n test cases
    if n <= 0:
        return
    t = n
    # choose dimensions so that n ~ t * (rows * cols), keep rows, cols >= 1
    base = max(1, int(n ** 0.5))
    rows = base
    cols = base
    # build deterministic grids for each test case
    allans = []
    for case_id in range(t):
        r = rows
        c = cols
        grid = []
        for i in range(r):
            row = []
            for j in range(c):
                # deterministic value depending on n, case_id, i, j
                val = (n * 17 + case_id * 31 + i * 7 + j * 13 + i * j * 3) % 1000003
                row.append(val)
            grid.append(row)
        ans = solve_single_case(r, c, grid)
        allans.append(ans)
    multiLineArrayPrint(allans)


if __name__ == "__main__":
    main(5)