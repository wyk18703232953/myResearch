from collections import defaultdict


def solve_generated(rows, cols, grid):
    n, m = rows, cols
    cnt = defaultdict(int)
    res = []
    for i in range(n):
        A = grid[i]
        res.append(A)
        for j in range(m):
            if A[j]:
                cnt[j] += 1
    valid = False
    for r in res:
        j = [i for i in range(m) if r[i]]
        if all(cnt[i] > 1 for i in j):
            valid = True
            break
    if valid:
        # print("YES")
        pass

    else:
        # print("NO")
        pass


def main(n):
    # Interpret n as both number of rows and columns of the binary matrix
    rows = n
    cols = n

    # Deterministically generate a rows x cols binary matrix
    # Example pattern: A[i][j] = 1 if (i + j) % 3 != 0 else 0
    grid = [[1 if (i + j) % 3 != 0 else 0 for j in range(cols)] for i in range(rows)]

    t = 1
    while t:
        t -= 1
        solve_generated(rows, cols, grid)


if __name__ == "__main__":
    main(5)