import math

def solve_single_case(a):
    n = len(a)
    m = len(a[0]) if n > 0 else 0
    inf = -float("inf")
    y = 1 << n
    dp = [[0] + [inf] * (y - 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for shift in range(n):
            for mask1 in range(y):
                for mask2 in range(y):
                    new = mask1 ^ mask2
                    if new & mask1:
                        continue
                    mm, add = 1, 0
                    for x in range(n):
                        if mm & new:
                            tt = x + shift
                            if tt >= n:
                                tt -= n
                            add += a[tt][i - 1]
                        mm <<= 1
                    dp[i][mask2] = max(dp[i][mask2], dp[i - 1][mask1] + add)
    return dp[m][y - 1]

def generate_matrix(n):
    # n controls both number of rows and columns: n x n
    # a[i][j] = (i * 131 + j * 37 + 7) % 1000 - 500  (deterministic)
    size = n
    a = []
    for i in range(size):
        row = []
        for j in range(size):
            val = (i * 131 + j * 37 + 7) % 1000 - 500
            row.append(val)
        a.append(row)
    return a

def main(n):
    # Use n as the matrix dimension n x n, single test case
    a = generate_matrix(n)
    ans = solve_single_case(a)
    print(ans)

if __name__ == "__main__":
    main(4)