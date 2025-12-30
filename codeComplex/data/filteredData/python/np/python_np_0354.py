# Converted version: no input(), parametrized by n, with generated test data.

import random

def main(n):
    # Generate test data based on n
    # You can adjust the data generation rules as needed.
    #
    # Original program:
    #   for _ in range(t):
    #       n, m
    #       a: n x m matrix
    #
    # Here we create a single test instance:
    #   - number of rows  = n
    #   - number of columns m = n (can be changed)
    #   - a[i][j] random integers in some range (e.g. [-10, 10])
    m = n
    a = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]

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

    # Return the result instead of printing (can be printed by caller)
    return dp[m][y - 1]


if __name__ == "__main__":
    # Example: run main with n = 4
    result = main(4)
    print(result)