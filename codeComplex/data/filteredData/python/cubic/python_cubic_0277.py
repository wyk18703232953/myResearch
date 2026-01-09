import math
from collections import Counter, defaultdict, deque
from io import BytesIO, IOBase

# Global variables to keep original structure
r = []
g = []
b = []
rl = bl = gl = 0
dp = []


def rec(i, j, k):
    if (i == rl and j == bl) or (i == rl and k == gl) or (k == gl and j == bl):
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    x = r[i] * b[j]
    y = b[j] * g[k]
    z = r[i] * g[k]
    if x > 0:
        x += rec(i + 1, j + 1, k)
    if y > 0:
        y += rec(i, j + 1, k + 1)
    if z > 0:
        z += rec(i + 1, j, k + 1)
    dp[i][j][k] = max(x, y, z)
    return dp[i][j][k]


def generate_arrays(n):
    # Map n to lengths of the three arrays; simple deterministic split
    rl = max(1, n // 3)
    bl = max(1, (n + 1) // 3)
    gl = max(1, (n + 2) // 3)

    # Deterministic positive integers; pattern chosen to be simple but non-constant
    r = [i % 7 + 1 for i in range(1, rl + 1)]
    b = [i % 9 + 1 for i in range(1, bl + 1)]
    g = [i % 11 + 1 for i in range(1, gl + 1)]
    return rl, bl, gl, r, b, g


def main(n):
    global r, g, b, rl, bl, gl, dp

    rl, bl, gl, r, b, g = generate_arrays(n)
    # Original code appends a zero sentinel
    r = r + [0]
    b = b + [0]
    g = g + [0]

    dp = [[[-1 for _ in range(gl + 1)] for _ in range(bl + 1)] for _ in range(rl + 1)]
    r.sort(reverse=True)
    b.sort(reverse=True)
    g.sort(reverse=True)

    result = rec(0, 0, 0)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(10)