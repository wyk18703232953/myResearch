def f(lst, num):
    # rotate list left by num positions
    n = len(lst)
    num %= n
    return lst[num:] + lst[:num]


def generate_test_case(idx, n):
    # Deterministically generate (row, col, matrix) based on idx and n
    row = n
    col = min(4, max(1, (idx % 4) + 1))
    matrix = []
    for r in range(row):
        # each element is a simple function of (idx, r, c) to keep it deterministic
        line = [(idx + 1) * (r + 1) + (c + 1) * (idx + r + 1) for c in range(col)]
        matrix.append(line)
    return row, col, matrix


def solve_one(row, col, matrix):
    # transform matrix into list of columns as lists
    lst = [[matrix[r][c] for r in range(row)] for c in range(col)]
    # sort columns by their max value descending
    lst.sort(key=lambda x: max(x), reverse=True)

    ans = float('-inf')
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    if col >= 1:
                        aa = f(lst[0], a)
                    else:
                        aa = (0,) * row
                    if col >= 2:
                        bb = f(lst[1], b)
                    else:
                        bb = (0,) * row
                    if col >= 3:
                        cc = f(lst[2], c)
                    else:
                        cc = (0,) * row
                    if col >= 4:
                        dd = f(lst[3], d)
                    else:
                        dd = (0,) * row

                    cur = 0
                    for j in range(row):
                        cur += max(aa[j], bb[j], cc[j], dd[j])
                    if cur > ans:
                        ans = cur
    return ans


def main(n):
    # n controls both number of test cases and matrix size
    if n <= 0:
        return
    t = n
    results = []
    for i in range(t):
        row, col, matrix = generate_test_case(i, n)
        res = solve_one(row, col, matrix)
        results.append(res)
    for x in results:
        print(x)


if __name__ == "__main__":
    # example deterministic call
    main(5)