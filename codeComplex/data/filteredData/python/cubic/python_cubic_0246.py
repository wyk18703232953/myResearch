from math import *
from collections import *
from decimal import Decimal
from heapq import *
from bisect import *


def main(n):
    # Interpret n as total number of elements across three lists
    # Split n into r, g, b as evenly as possible
    if n < 3:
        r = n
        g = 0
        b = 0

    else:
        base = n // 3
        rem = n % 3
        r = base + (1 if rem > 0 else 0)
        g = base + (1 if rem > 1 else 0)
        b = base

    # Deterministically generate lists rl, gl, bl based on r, g, b
    rl = [i + 1 for i in range(r)]
    gl = [2 * (i + 1) for i in range(g)]
    bl = [3 * (i + 1) for i in range(b)]

    rl.sort()
    gl.sort()
    bl.sort()

    # 3D DP array, same logic as original program
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i + j + k < 2:
                    continue
                best = dp[i][j][k]
                if i and j:
                    val = dp[i - 1][j - 1][k] + rl[i - 1] * gl[j - 1]
                    if val > best:
                        best = val
                if j and k:
                    val = dp[i][j - 1][k - 1] + gl[j - 1] * bl[k - 1]
                    if val > best:
                        best = val
                if i and k:
                    val = dp[i - 1][j][k - 1] + rl[i - 1] * bl[k - 1]
                    if val > best:
                        best = val
                dp[i][j][k] = best

    result = dp[r][g][b]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(30)