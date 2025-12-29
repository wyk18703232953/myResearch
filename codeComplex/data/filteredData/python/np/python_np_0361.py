import random

def solve_case(n: int, m: int, mat):
    # build columns
    col = [[] for _ in range(m)]
    for j in range(n):
        for k, item in enumerate(mat[j]):
            col[k].append(item)

    # find max column values and keep column data
    colmax = []
    for line in col:
        colmax.append([max(line), line])
    colmax.sort(reverse=True)
    colmax = colmax[:n]  # keep top-n columns

    ans = 0
    # brute force over all rotations encoded in base-n with (n-1) digits
    for j in range(n ** (n - 1)):
        index = j
        rot = [0]
        for _ in range(n - 1):
            rot.append(index % n)
            index //= n

        ret = 0
        for l in range(n):
            val = 0
            for k in range(len(colmax)):
                val = max(val, colmax[k][1][(l + rot[k]) % n])
            ret += val
        ans = max(ans, ret)
    return ans


def main(n: int):
    """
    n: problem scale (number of rows and also the number of selected columns)

    We will:
    - set m >= n (e.g. m = n or some function of n)
    - randomly generate an n x m matrix of integers
    - run the original logic once and return the answer
    """
    # you can change the following generation rules as needed
    m = n  # or e.g. m = max(1, n + n // 2)
    # generate test matrix with values in [0, 100]
    mat = [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]

    ans = solve_case(n, m, mat)
    print(ans)
    return ans


if __name__ == "__main__":
    # example run with n = 3
    main(3)